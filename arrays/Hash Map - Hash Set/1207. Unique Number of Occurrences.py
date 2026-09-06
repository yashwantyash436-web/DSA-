class Solution(object):
    def uniqueOccurrences(self, arr):

        # Dictionary to store:
        # number → frequency
        freq = {}

        # Count the frequency of each number
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Set to store frequencies we have already seen
        seen = set()

        # Go through each number and its frequency
        for num, count in freq.items():

            # If this frequency already exists,
            # two numbers have the same frequency
            if count in seen:
                return False

            # Otherwise, remember this frequency
            seen.add(count)

        # Every frequency was unique
        return True