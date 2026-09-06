class Solution:
    def searchRange(self, nums, target):

        def binary_search(find_first):

            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:

                    # We found target.
                    # Save this position first.
                    answer = mid

                    if find_first:
                        # Looking for FIRST occurrence.
                        # Keep searching LEFT.
                        right = mid - 1
                    else:
                        # Looking for LAST occurrence.
                        # Keep searching RIGHT.
                        left = mid + 1

                elif nums[mid] < target:

                    # Target is bigger.
                    # Search RIGHT.
                    left = mid + 1

                else:

                    # Target is smaller.
                    # Search LEFT.
                    right = mid - 1

            return answer

        # Find the FIRST occurrence
        first = binary_search(True)

        # Find the LAST occurrence
        last = binary_search(False)

        return [first, last]