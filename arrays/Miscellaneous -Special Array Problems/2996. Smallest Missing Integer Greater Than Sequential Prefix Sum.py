class Solution:
    def missingInteger(self, nums):
        total = nums[0]

        # Find the sum of the longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Store all numbers in a set for fast lookup
        num_set = set(nums)

        # Find the smallest missing integer
        while total in num_set:
            total += 1

        return total