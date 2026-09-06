class Solution:
    def search(self, nums, target):

        # Start Binary Search from the whole array
        left = 0
        right = len(nums) - 1

        while left <= right:

            # Find the middle position
            mid = (left + right) // 2

            # If middle is the target, we are done
            if nums[mid] == target:
                return mid

            # -----------------------------------------
            # Check if the LEFT half is sorted
            # -----------------------------------------
            if nums[left] <= nums[mid]:

                # LEFT half is sorted

                # Check if target is inside the sorted LEFT half
                if nums[left] <= target < nums[mid]:

                    # Target is on the LEFT
                    right = mid - 1

                else:

                    # Target is on the RIGHT
                    left = mid + 1

            # -----------------------------------------
            # Otherwise, the RIGHT half is sorted
            # -----------------------------------------
            else:

                # RIGHT half is sorted

                # Check if target is inside the sorted RIGHT half
                if nums[mid] < target <= nums[right]:

                    # Target is on the RIGHT
                    left = mid + 1

                else:

                    # Target is on the LEFT
                    right = mid - 1

        # Target was not found
        return -1