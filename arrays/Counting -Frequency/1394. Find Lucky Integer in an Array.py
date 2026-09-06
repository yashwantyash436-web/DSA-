class Solution(object):
    def findLucky(self, arr):
        # Dictionary to store:
        # number → frequency
        freq = {}

        # Count the frequency of every number
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Start with -1 in case there is no lucky number
        largest = -1

        # Go through each number and its frequency
        for num, count in freq.items():

            # A lucky number's value must equal its frequency
            if num == count:

                # Keep the largest lucky number found so far
                largest = max(largest, num)

        # Return the largest lucky number
        # If none was found, this remains -1
        return largest