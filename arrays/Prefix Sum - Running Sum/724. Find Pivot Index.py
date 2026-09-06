class Solution(object):
    def pivotIndex(self, nums):

        # Find the total sum of the array
        total_sum = sum(nums)

        # Store the running sum of the left side
        left_sum = 0

        # Traverse every element
        for i in range(len(nums)):

            # Calculate the right sum
            right_sum = total_sum - left_sum - nums[i]

            # Check if both sums are equal
            if left_sum == right_sum:
                return i

            # Update the left sum for the next iteration
            left_sum += nums[i]

        # No pivot index found
        return -1


# =====================================================
# My Brute Force Approach (Using append() and sum())
# =====================================================

# class Solution(object):
#
#     def pivotIndex(self, nums):
#
#         for i in range(len(nums)):
#
#             left = []
#             right = []
#
#             # Store left elements
#             for j in range(i):
#                 left.append(nums[j])
#
#             # Store right elements
#             for j in range(i + 1, len(nums)):
#                 right.append(nums[j])
#
#             # Compare sums
#             if sum(left) == sum(right):
#                 return i
#
#         return -1

#mine solution 