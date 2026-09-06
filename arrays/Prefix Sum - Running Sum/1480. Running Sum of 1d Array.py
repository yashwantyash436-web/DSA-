class Solution:
    def runningSum(self, nums):

        # Input:
        # nums = [1, 2, 3, 4]

        # Step 1: Create an empty array to store the answers
        ans = []
        # ans = []

        # Step 2: Create a variable to store the running total
        running_sum = 0
        # running_sum = 0

        # Step 3: Visit every number one by one
        for i in nums:

            # -----------------------------
            # First Iteration
            # i = 1
            # running_sum = 0 + 1 = 1
            # running_sum = 1
            # -----------------------------

            # -----------------------------
            # Second Iteration
            # i = 2
            # running_sum = 1 + 2 = 3
            # running_sum = 3
            # -----------------------------

            # -----------------------------
            # Third Iteration
            # i = 3
            # running_sum = 3 + 3 = 6
            # running_sum = 6
            # -----------------------------

            # -----------------------------
            # Fourth Iteration
            # i = 4
            # running_sum = 6 + 4 = 10
            # running_sum = 10
            # -----------------------------

            # Add the current number to the previous running total
            running_sum = running_sum + i

            # Store the current running total in the answer array
            ans.append(running_sum)

            # After each iteration:
            # Iteration 1 -> ans = [1]
            # Iteration 2 -> ans = [1, 3]
            # Iteration 3 -> ans = [1, 3, 6]
            # Iteration 4 -> ans = [1, 3, 6, 10]

        # Step 4: Return the final answer
        return ans
        #answer

        # Final Output:
        # [1, 3, 6, 10]