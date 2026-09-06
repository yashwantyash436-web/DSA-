class Solution(object):
    def intersection(self, nums1, nums2):
        freq = {}       # Store each number and its frequency in nums1
        result = []

        # Count frequency of elements in nums1
        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Check elements in nums2
        for num in nums2:
            if num in freq and freq[num] > 0:

                # Add only if this number is not already in result
                if num not in result:
                    result.append(num)

                # Mark this occurrence as used
                freq[num] -= 1

        return result