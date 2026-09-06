class Solution:
    def thirdMax(self, nums):

        # Step 1: Remove duplicate values because the question says "distinct"
        unique_no = list(set(nums))

        # Example:
        # nums = [2,2,3,1]
        # unique_no = [2,3,1]

        # Step 2: Sort the unique numbers in ascending order
        unique_no.sort()

        # Example:
        # [1,2,3]

        # Step 3: Reverse the list so the largest numbers come first
        unique_no.reverse()

        # Example:
        # [3,2,1]

        # Step 4:
        # If there are at least 3 distinct numbers,
        # return the third maximum.
        if len(unique_no) >= 3:
            return unique_no[2]

        # Step 5:
        # Otherwise return the largest number.
        else:
            return unique_no[0]