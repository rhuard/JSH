import os

class Configurer:
    """
    This class is responsible for reading in the .jshrc and configuring
    JSH accordingly.
    """
    def __init__(self):
        self.conf={
            "dead child" : False,
            "prompt" : ""
        }

    def configure(self):
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
                        #import pdb; pdb.set_trace()
                        pieces[i] = pieces[i].strip() #shave whitespace

                    self.conf[pieces[0]] = pieces[1]

        except:
            #could not find the ~/.jshrc file
            print("error in configuration")

        return self.conf
