class Solution:
    def twoSum(self, nums, target):

        current_index_value = {}

        for index, num in enumerate(nums):

            complement = target - num

            if complement in current_index_value:
                return [current_index_value[complement], index]

            else:
                current_index_value[num] = index

        return []   