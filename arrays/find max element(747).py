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