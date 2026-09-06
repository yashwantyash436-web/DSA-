class Solution:
    def maxAscendingSum(self, nums):

        # Start with the first number
        current_sum = nums[0]

        # This stores the biggest sum we have found
        max_sum = nums[0]

        # Start checking from the second number
        for i in range(1, len(nums)):

            # If the current number is greater than
            # the previous number, the ascending subarray continues
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]

            else:
                # Ascending sequence is broken
                # Start a new subarray from the current number
                current_sum = nums[i]

            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum