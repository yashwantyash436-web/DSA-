class Solution(object):
    def moveZeroes(self, nums):

        left = 0

        # right travels through the entire array
        for right in range(len(nums)):

            # We only care when we find a non-zero
            if nums[right] != 0:

                # Put the non-zero number at left
                nums[left], nums[right] = nums[right], nums[left]

                # Next non-zero should go to the next position
                left += 1

        return nums