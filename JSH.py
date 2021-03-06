import os
import subprocess
import shutil
from Conf import Prompt
from JSHUtil import Input, IORedirect
from Conf import Configure as config

class JSH:

    def __init__(self):
        """
        Read in configuration file and configure jsh options
        """
        #conf is a dictonary of values which can be modified in .jshrc
        conf = config.Configurer()
        self.var = conf.Configure()
        self._prompt = Prompt.JSHPrompt(self.var["prompt"])
        self._ih = Input.InputHandler()

    def _searchPath(self, cmd):
        """
        Searches the PATH variable to the asked
        executable file. Returns None if not found.
        If found returns a string of the path, which
        can be used in os.exec*
        """
        return shutil.which(cmd)

    def _PrintDeadChild(self, cpid, s):
        if( "True" == self.var["dead child"]):
            print("child died :(    " + str(cpid) + " status: " + str(s))
        else:
            pass

    def _Process(self, cmd):
        """
        Highest level of processing the command. This
        is what is called by external files
        """
        pieces = self._ih.Process(cmd)
        if "cd" == pieces[0]:
            if 1 < len(pieces):
                os.chdir(pieces[1])
            else:
                os.chdir('/')
        else:
            stin = None
            stout = None
            sterr = None
            #check for IO redirect
            redirect = IORedirect.IO_redirection(pieces)
            #input redirection
            if True == redirect[0]:
                stin = open(redirect[3], "r")
            if True == redirect[1]:
                stout = open(redirect[4], "w")
            if True == redirect[2]:
                stout = open(redirect[5], "a")

            subprocess.call(pieces, stdin = stin, stdout = stout)


    def Run(self):
        while(True):
            self._prompt.PrintPrompt()
            cmd = input()

            if("exit" == cmd):
                exit()
            elif("" == cmd):
                pass
            elif(cmd.isspace()):
                pass
            else:
                self._Process(cmd)
