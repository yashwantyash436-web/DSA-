# 747. Largest Number At Least Twice of Others
# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

# Example 1:

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
 

# Constraints:

# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.

class Solution(object):
    def dominantIndex(self, nums):

        # Keep track of the largest value
        max_value = -1

        # Keep track of the second-largest value
        second_value = -1

        # Keep track of the index of the largest value
        max_index = -1

        # Go through every number
        for index, num in enumerate(nums):

            # If we found a new largest number
            if num > max_value:

                # Old largest becomes second-largest
                second_value = max_value

                # Update largest number
                max_value = num

                # Remember its index
                max_index = index

            # Otherwise, check if it is the second-largest
            elif num > second_value:
                second_value = num

        # Check whether the largest is at least
        # twice the second-largest
        if max_value >= second_value * 2:
            return max_index

        # Otherwise, no dominant number exists
        return -1