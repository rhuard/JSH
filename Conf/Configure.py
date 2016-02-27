import os

class Configurer:
    """
    This class is responsible for reading in the .jshrc and configuring
    JSH accordingly.
    """
    def __init__(self):
        self._conf={
            "dead child" : False,
            "prompt" : ""
        }
    def _AddVar(self, var, value):
        if var in self._conf:
            self._conf[var] = value
        else:
            print("error with jshrc unknown setting: " + str(var))

    def Configure(self):
        """
        called on startup of JSH, can also be called when the file has been
        changed to update configuration
        """
        try:
            rc = os.environ["HOME"] + "/.jshrc" 
            with open(rc, "r") as rcfile:
                for line in rcfile:
                    #first get rid of the comments
                    #import pdb; pdb.set_trace()
                    comment = line.find("#")
                    if(comment != -1):
                        line = line[:comment]
                    pieces = line.split("=");
                    if(pieces==[""] or pieces==["\n"]):
                        continue

                    for i in range(len(pieces)):
                        pieces[i] = pieces[i].strip() #shave whitespace

                    self._AddVar(pieces[0], pieces[1])

        except:
            #could not find the ~/.jshrc file
            print("error in configuration")

        return self._conf
