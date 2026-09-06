class Solution:
    def maximumWealth(self, accounts):

        # Store the maximum wealth found so far
        max_wealth = 0

        # Visit each customer's accounts (one row at a time)
        for customer in accounts:

            # Calculate the total wealth of this customer
            cus_wealth = sum(customer)

            # If this customer is richer than the current maximum
            if cus_wealth > max_wealth:

                # Update the maximum wealth
                max_wealth = cus_wealth

        # Return the richest customer's wealth
        return max_wealth