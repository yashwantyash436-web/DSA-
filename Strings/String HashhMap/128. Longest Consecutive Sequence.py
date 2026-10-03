class Solution:
    def longestConsecutive(self, nums):

        # Put all numbers into a set.
        # A set allows us to quickly check whether a number exists.
        num_set = set(nums)

        # This stores the longest consecutive sequence found so far.
        longest = 0

        # Check every number in the set.
        for num in num_set:

            # If num - 1 does NOT exist,
            # then num is the START of a consecutive sequence.
            if num - 1 not in num_set:

                # We found the beginning of a sequence.
                length = 1

                # Keep checking the next consecutive numbers.
                next_num = num + 1

                while next_num in num_set:

                    # We found the next number in the sequence.
                    length += 1

                    # Move to the next number.
                    next_num += 1

                # Update the longest sequence found so far.
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence.
        return longest
        #leave