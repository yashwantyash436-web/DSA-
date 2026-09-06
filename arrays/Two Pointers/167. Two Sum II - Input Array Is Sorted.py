class Solution:
    def twoSum(self, numbers, target):

        # Start one pointer from the left
        left = 0

        # Start the other pointer from the right
        right = len(numbers) - 1

        # Keep checking until the pointers meet
        while left < right:

            current_sum = numbers[left] + numbers[right]

            # We found the target
            if current_sum == target:
                # LeetCode wants 1-based indexes
                return [left + 1, right + 1]

            # Sum is too small → need a bigger number
            elif current_sum < target:
                left += 1

            # Sum is too large → need a smaller number
            else:
                right -= 1