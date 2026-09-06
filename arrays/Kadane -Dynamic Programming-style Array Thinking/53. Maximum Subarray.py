class Solution(object):
    def maxSubArray(self, nums):

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            # Choose: start a new subarray OR continue the current one
            current_sum = max(num, current_sum + num)

            # Keep track of the best sum found so far
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# ============================================================
# MY ORIGINAL CODE / ATTEMPT
# ============================================================

# class Solution(object):
#
#     def maxSubArray(self, nums):
#
#         current_sum = 0
#         max_sum = 0
#
#         for num in nums:
#
#             current_sum = max(num, current_sum + num)
#
#             if current_sum > max_sum:
#                 max_sum = current_sum
#
#         return max_sum