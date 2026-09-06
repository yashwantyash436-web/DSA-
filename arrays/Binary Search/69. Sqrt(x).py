class Solution:
    def mySqrt(self, x):

        # If x is 0 or 1, the square root is already x.
        # Example:
        # x = 0 → √0 = 0
        # x = 1 → √1 = 1
        if x < 2:
            return x

        # We will search for the answer between left and right.
        # For x = 8:
        # left = 1
        # right = 8 // 2 = 4
        left = 1
        right = x // 2

        # Keep searching while there is still a valid
        # search area.
        while left <= right:

            # Find the middle number.
            # Example:
            # left = 1, right = 4
            # mid = (1 + 4) // 2 = 2
            mid = (left + right) // 2

            # Check the square of the middle number.
            # Example:
            # mid = 2
            # square = 2 × 2 = 4
            square = mid * mid

            # If mid × mid is exactly x,
            # we found the square root.
            # Example:
            # x = 4, mid = 2
            # 2 × 2 = 4 → return 2
            if square == x:
                return mid

            # If the square is smaller than x,
            # mid is too small.
            #
            # Example:
            # x = 8
            # mid = 2
            # 2 × 2 = 4
            #
            # We need to search on the RIGHT side.
            elif square < x:
                left = mid + 1

            # If the square is bigger than x,
            # mid is too big.
            #
            # Example:
            # x = 8
            # mid = 3
            # 3 × 3 = 9
            #
            # We need to search on the LEFT side.
            else:
                right = mid - 1

        # If we didn't find an exact square root,
        # right will contain the largest number whose
        # square is smaller than x.
        #
        # Example:
        # x = 8
        #
        # 2 × 2 = 4  ✅
        # 3 × 3 = 9  ❌
        #
        # Therefore the answer is 2.
        return right
        #learning today 