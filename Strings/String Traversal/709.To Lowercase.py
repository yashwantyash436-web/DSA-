class Solution:
    def toLowerCase(self, s):

        result = ""

        # Traverse every character
        for ch in s:

            # Check whether character is uppercase
            if 'A' <= ch <= 'Z':

                # Convert uppercase → lowercase
                result += chr(ord(ch) + 32)

            else:
                # Already lowercase or another character
                result += ch
#one day leave 
        return result