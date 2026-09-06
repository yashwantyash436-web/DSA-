class Solution:
    def findNumbers(self, nums):

        # Store how many numbers have an even number of digits
        count = 0

        # Visit every number in the array
        for num in nums:

            # Convert the number into a string and count its digits
            digits = len(str(num))

            # Check if the number of digits is even
            if digits % 2 == 0:
                count += 1

        # Return the total count
        return count