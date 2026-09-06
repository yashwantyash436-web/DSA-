class Solution:
    def findMaxAverage(self, nums, k):
        
        # Sum of the first k elements (first window)
        window_sum = sum(nums[:k])
        
        # Store the maximum sum found
        max_sum = window_sum
        
        # Slide the window through the array
        for i in range(k, len(nums)):
            
            # Remove the old left element
            # Add the new right element
            window_sum = window_sum - nums[i - k] + nums[i]
            
            # Update maximum sum
            max_sum = max(max_sum, window_sum)
        
        # Convert to float so division gives decimal result
        return float(max_sum) / k