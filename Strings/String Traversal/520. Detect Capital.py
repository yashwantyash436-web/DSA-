class Solution:
    def detectCapitalUse(self, word):

        uppercase_count = 0

        for ch in word:
            if 'A' <= ch <= 'Z':
                uppercase_count += 1

        if uppercase_count == len(word):
            return True

        if uppercase_count == 0:
            return True

        if uppercase_count == 1 and 'A' <= word[0] <= 'Z':
            return True

        return False