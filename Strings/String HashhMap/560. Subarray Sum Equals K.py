class Solution:
    def subarraySum(self, nums, k):
        
        # Stores the running total (prefix sum)
        prefix_sum = 0
        
        # Stores how many subarrays have a sum equal to k
        count = 0
        
        # Hash map:
        # key   = prefix sum
        # value = how many times we have seen that prefix sum
        #
        # 0:1 means we have seen a prefix sum of 0 once.
        # This helps us find subarrays that start from index 0.
        prefix_map = {0: 1}
        
        # Go through every number in the array
        for num in nums:
            
            # Add the current number to our running total
            prefix_sum += num
            
            # We need a previous prefix sum such that:
            #
            # current prefix - previous prefix = k
            #
            # Therefore:
            # previous prefix = current prefix - k
            needed = prefix_sum - k
            
            # If this required prefix sum existed before,
            # we have found one or more subarrays whose sum is k.
            if needed in prefix_map:
                count += prefix_map[needed]
            
            # Store the current prefix sum in the hash map.
            # If it already exists, increase its frequency by 1.
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        # Return the total number of subarrays whose sum equals k
        return count