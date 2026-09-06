class Solution(object):
    def majorityElement(self, nums):
        # Dictionary to store the frequency of each number
        count = {}

        # Total number of elements in the array
        n = len(nums)

        # Traverse through every number in the array
        for num in nums:

            # Increase the frequency of the current number
            # If num is not present, start its count from 0
            count[num] = count.get(num, 0) + 1

            # Check if the current number has appeared
            # more than half of the total array
            if count[num] > n / 2:
                return num