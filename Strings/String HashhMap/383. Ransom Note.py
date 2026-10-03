class Solution:
    def canConstruct(self, ransomNote, magazine):

        # Store how many times each character appears in magazine
        count = {}

        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Use one character from magazine for every character in ransomNote
        for ch in ransomNote:

            # Character is not available, or we already used all of it
            if ch not in count or count[ch] == 0:
                return False

            # Use one occurrence of this character
            count[ch] -= 1

        # Every required character was available
        return True