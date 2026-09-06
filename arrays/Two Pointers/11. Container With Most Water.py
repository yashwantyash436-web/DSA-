class Solution(object):
    def maxArea(self, height):

        # Start from the two ends of the array
        left = 0
        right = len(height) - 1

        # Store the maximum water found so far
        max_water = 0

        # Continue until the two pointers meet
        while left < right:

            # Width = distance between the two walls
            width = right - left

            # Water height is limited by the shorter wall
            container_height = min(height[left], height[right])

            # Calculate water for the current two walls
            water = width * container_height

            # Update maximum water if current container is bigger
            if water > max_water:
                max_water = water

            # Move the pointer at the shorter wall
            # because the shorter wall is limiting the water height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the largest amount of water found
        return max_water