class Solution:
    def firstUniqChar(self, s):

        frequency = {}

        # Count every character
        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        # Find the first character that appears once
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i

        return -1
        #leave