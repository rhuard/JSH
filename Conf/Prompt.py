import datetime
import os

class JSHPrompt:
    """
    This class will allow for customising the Prompt
    current support for:
        printing time in  H:M:S format - %t
        printing CWD - %PWD
        printing a space ' ' - %s
    """


    def __init__(self, prompt):
        self._prompt = prompt

    def _checkKeyword(self, prompt, keyphrase, replace):
        """
        Checks string passed in as prompt for a keyword, if
        found it replaces the keyphrase with the replace
        phrase.

        Prompt is the string you are searching through
        keywphrase is the target to replace
        replace is the prase to replace target with
        """
        index = prompt.find(keyphrase)
        if(index != -1):
            p = prompt.replace(keyphrase, replace)
        else:
            p = prompt
        return p


    def PrintPrompt(self):
        p = self._checkKeyword(self._prompt,
                "%t",datetime.datetime.now().strftime("[%H:%M:%S]"))
        p = self._checkKeyword(p, "%PWD", os.getcwd())
        p = self._checkKeyword(p, "%s", " ")
        print(p, end="")

