
class Solution:
    def maxProduct(self, nums):

        # At the beginning, the first number
        # is both our maximum and minimum product
        current_max = nums[0]
        current_min = nums[0]

        # Store the best answer found so far
        answer = nums[0]

        # Start from the second element
        for i in range(1, len(nums)):

            num = nums[i]

            # If num is negative, maximum and minimum
            # will swap because multiplying by negative
            # reverses their order
            if num < 0:
                current_max, current_min = current_min, current_max

            # Either:
            # 1. Start a new subarray from num
            # 2. Continue the previous subarray
            current_max = max(num, current_max * num)

            current_min = min(num, current_min * num)

            # Update the overall maximum product
            answer = max(answer, current_max)

        return answer

        # i took a leave of 