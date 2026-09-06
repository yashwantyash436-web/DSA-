class Solution(object):
    def largestAltitude(self, gain):

        current = 0
        highest = 0

        for g in gain:

            # Move to the next altitude
            current += g

            # Remember the highest altitude seen so far
            highest = max(highest, current)

        return highest