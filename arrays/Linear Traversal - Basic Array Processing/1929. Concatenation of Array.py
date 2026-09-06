class Solution:
    def getConcatenation(self, nums):

        # Create an empty array to store the answer
        ans = []

        # First time: copy every element from nums
        for i in nums:
            ans.append(i)

        # Second time: copy every element again
        for i in nums:
            ans.append(i)

        # Return the final concatenated array
        return ans
        