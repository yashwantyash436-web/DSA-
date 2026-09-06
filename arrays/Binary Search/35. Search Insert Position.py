class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target is bigger
            elif nums[mid] < target:
                left = mid + 1

            # Target is smaller
            else:
                right = mid - 1

        # Target was not found.
        # 'left' is now the correct insertion position.
        return left

        #ome more leave
        #i am skipping today also