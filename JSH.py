import os
import shutil
from jshutil import Prompt

class JSH:

    def __init__(self):
        """
        Read in configuration file and configure jsh options
        """
        #TODO: implement the .jshrc file
        #dictonary to keep track of jshenv. Stored in .jshrc
        self.var = {
                "dead child" : False
                }

        self.prompt = Prompt.JSHPrompt("%t>")

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
        if(self.var["dead child"]):
            print("child died :(    " + str(cpid) + " status: " + str(s))
        else:
            pass

    def Process(self, cmd):
        """
        Highest level of processing the command. This
        is what is called by external files
        """
        #TODO: add support for "" and ''
        pieces = cmd.split()
        execute = self._searchPath(pieces[0])

        if(None != execute):

            newpid = os.fork()

            if(0 == newpid):
                self._run_child(execute, pieces[0:])
            else:
                cpid,s = os.wait()
                self._PrintDeadChild(cpid, s)
        else:
            print("unknwon command please try again")
