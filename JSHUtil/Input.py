class InputHandler:
    """
    This class is responsible for handling all of the input and generating a
    list of all of the pieces
    """

    def _CheckWrappingChars(self, s, ch):
        """
        This is a generic method to check a line of text
        for a particuar warapping chars. For examle,
        quite marks or paranthesis
        s is the string to parse and quote is the wrapping char
        """

        first = s.find(ch)
        if(-1 == first):
            return False,s
        else:
            second = s.find(ch, first+1)
            pieces = s[:first].split()
            pieces.append(s[first:second+1])
            pieces.append(s[second+1:])
            return True,pieces




    def Process(self, cmd):

        hasquotes,pieces = self._CheckWrappingChars(cmd, '"')
        if(False == hasquotes):
            hasquotes,pieces = self._CheckWrappingChars(cmd, "'")

        if(False == hasquotes):
            pieces = cmd.split()

        return pieces
