import os
import shutil
from Conf import Prompt
from JSHUtil import Input
from Conf import Configure as config

class JSH:

    def __init__(self):
        """
        Read in configuration file and configure jsh options
        """
        #TODO: implement the .jshrc file
        #dictonary to keep track of jshenv. Stored in .jshrc
        conf = config.Configurer()
        self.var = conf.Configure() 

        self._prompt = Prompt.JSHPrompt(self.var["prompt"])
        self._ih = Input.InputHandler()

    def _run_child(self, cmd, args):
        """
        Exec the child process to run the given command
        """
        os.execv(cmd, args)

    def _io_check(self, args_list):
        """
        Scans the given input for |, <, >, and >>
        and sets up files accordingly
        """
        pass

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
        execute = self._searchPath(pieces[0])

        if(None != execute):

            newpid = os.fork()
            plen = len(pieces)
            if(0 == newpid):
                if pieces[plen-1] == '&':
                    self._run_child(execute, pieces[0:plen-1]) # exclude the '&' to execute correctly
                else:
                    self._run_child(execute, pieces[0:])
            else:
                if pieces[len(pieces)-1] != '&':
                    cpid,s = os.wait()
                    self._PrintDeadChild(cpid, s)
        else:
            if("cd" == pieces[0]):
                if len(pieces) > 1:
                    os.chdir(pieces[1])
                else:
                    os.chdir('/')
            else:
                print("unknown command please try again")




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
