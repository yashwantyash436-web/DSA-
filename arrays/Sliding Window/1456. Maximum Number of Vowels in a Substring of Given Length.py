class Solution:
    def maxVowels(self, s, k):

        vowels = "aeiou"

        # Count vowels in the first window
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        # This is the best count we have found so far
        max_count = count

        # Start sliding the window
        for i in range(k, len(s)):

            # Remove the character leaving the window
            if s[i - k] in vowels:
                count -= 1

            # Add the new character entering the window
            if s[i] in vowels:
                count += 1

            # Keep the maximum vowel count
            max_count = max(max_count, count)

        return max_count

        # i took a leave of add another submission 