class Solution:
    def numIdenticalPairs(self, nums):

        # Store the number of good pairs
        count = 0

        # Pick one element at a time
        for i in range(len(nums)):

            # Compare it with every element to its right
            for j in range(i + 1, len(nums)):

                # Check if both values are equal
                if nums[i] == nums[j]:

                    # If yes, increase the count
                    count += 1

        # Return the total number of good pairs
        return count