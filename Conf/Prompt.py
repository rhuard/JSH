import datetime
import os

class JSHPrompt:
    """
    This class will allow for customising the Prompt
    current support for:
        printing time in  H:M:S format - %t
        printing CWD - %PWD
    """


    def __init__(self, prompt):
        self._prompt = prompt

    def _checkTime(self, prompt):
        """
        checks for the time option in the prompt
        %t. If found it will return a modified prompt
        with the time in place of the %t
        """
        index = prompt.find("%t")
        if(index != -1):
            p = prompt.replace("%t",
                    datetime.datetime.now().strftime("[%H:%M:%S]"))
        else:
            p = prompt
        return p

    def _checkPWD(self, prompt):
        """
        Checks for the pwd option in the prompt: %PWD
        if it is found, this will return a modified prompt
        with the wd in place of the %PWD
        """
        index = prompt.find("%PWD")
        if(index != -1):
            p = prompt.replace("%PWD", os.getcwd())
        else:
            p = prompt
        return p


    def PrintPrompt(self):
        p = self._checkTime(self._prompt)
        p = self._checkPWD(p)
        print(p, end=" ")

