class Solution(object):
    def isIsomorphic(self, s, t):

        # Save the original strings
        string_s = s
        string_t = t

        # Now use s and t as dictionaries
        s = {}
        t = {}

        for a, b in zip(string_s, string_t):

            if a in s and s[a] != b:
                return False

            if b in t and t[b] != a:
                return False

            s[a] = b
            t[b] = a

        return True