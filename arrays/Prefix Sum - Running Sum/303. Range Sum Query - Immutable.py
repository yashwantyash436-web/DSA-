#class NumArray:

 #   def __init__(self, nums):
        # Build the prefix sum array
 #       self.prefix = [0]

  #      for num in nums:
   #         self.prefix.append(self.prefix[-1] + num)

  #  def sumRange(self, left, right):
        # Sum from left to right
    #    return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums):
        # Create an empty list to store prefix sums.
        #
        # Example:
        # nums = [-2, 0, 3, -5, 2, -1]
        #
        # We will eventually build:
        # prefix = [-2, -2, 1, -4, -2, -3]
        self.prefix = []

        # 'cur' means current/running sum.
        # We start at 0 because we haven't added anything yet.
        cur = 0

        # Go through every number in nums one by one.
        #
        # Example:
        # n = -2
class NumArray:

    def __init__(self, nums):

        # Create an empty list for prefix sums
        self.prefix = []

        # Running/current sum
        cur = 0

        # Go through every number
        for n in nums:

            # Add current number to running sum
            cur += n

            # Store the running sum
            self.prefix.append(cur)


    def sumRange(self, left, right):

        # Sum from index 0 up to the right index
        rightSum = self.prefix[right]

        # Sum of everything BEFORE the left index
        # If left is 0, there is nothing before it
        leftSum = self.prefix[left - 1] if left > 0 else 0

        # Remove the unwanted part
        return rightSum - leftSum