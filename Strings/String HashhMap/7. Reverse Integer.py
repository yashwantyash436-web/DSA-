class Solution:
    def reverse(self, x) :

        # Remember whether the original number was negative
        sign = -1 if x < 0 else 1

        # Work with the positive version
        x = abs(x)

        # This will store the reversed number
        reverse = 0

        # Extract digits one by one
        while x != 0:

            # Take the last digit
            digit = x % 10

            # Remove the last digit
            x //= 10

            # Add the digit to the reversed number
            reverse = reverse * 10 + digit

        # 32-bit signed integer range:
        # -2^31 to 2^31 - 1
        if reverse > 2**31 - 1:
            return 0

        # Put the original sign back
        return sign * reverse
        #leave