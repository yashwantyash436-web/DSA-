class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums)):
            # If the current smallest number is > 0, no triplet can sum to 0
            if nums[i] > 0:
                break
                
            # Step 2: Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Two-pointer setup
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for the second position
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate elements for the third position
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
        #today revise