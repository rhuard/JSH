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
                    comment = line.find("#")
                    #find the comments in the line
                    if(comment != -1): #if there were comments
                        line = line[:comment] #slice out the line
                    pieces = line.split("="); #get the vars and variables
                    if(pieces==[""] or pieces==["\n"]):#make sure the pieces ...
                        continue #... are not just a new line or the empty string

                    for i in range(len(pieces)):
                        pieces[i] = pieces[i].strip() #shave whitespace
                        pieces[i] = pieces[i].encode().decode('unicode_escape') #strip off the first \ that is put
                                            #on escaped chars when they are read in. Example when a litteral \n is
                                            #in the .jshrc it will be read in as \\n. This turns it back to \n

                    self._AddVar(pieces[0], pieces[1])#add the var to the dictonary

        except:
            #could not find the ~/.jshrc file
            print("error in configuration: .jshrc was not found")

        return self._conf
