class Solution(object):
    def leftRightDifference(self, nums):

        answer = []

        # ---------------- LEFT SUM ----------------
        left_sum = 0
        left_arr = []

        for i in range(len(nums)):
            left_arr.append(left_sum)
            left_sum += nums[i]

        # ---------------- RIGHT SUM ----------------
        right_sum = 0
        right_arr = []

        for i in range(len(nums) - 1, -1, -1):
            right_arr.append(right_sum)
            right_sum += nums[i]

        # Right array was created from right to left,
        # so reverse it to match the original indexes.
        right_arr.reverse()

        # ---------------- DIFFERENCE ----------------
        for i in range(len(nums)):
            difference = abs(left_arr[i] - right_arr[i])
            answer.append(difference)

        return answer


# ============================================================
# MY ORIGINAL CODE / ATTEMPT
# Kept here for revision
# ============================================================

# class Solution(object):
#
#     def leftRightSum(self, nums):
#
#         answer = []
#         left_sum = 0
#         left_arr = []
#
#         for i in nums[0, i-1]:
#             left_sum += sum(i)
#             left_arr += append(left_sum)
#
#         right_sum = 0
#         right_arr = []
#
#         for i in nums[i+1, 0]:
#             right_sum += sum(i)
#             right_arr += append(right_sum)
#
#         difference = abs(left_arr - right_arr)
#         answer.append(difference)
#
#         return answer
#1 revision 