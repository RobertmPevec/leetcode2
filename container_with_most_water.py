class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        current_width = len(height) - 1
        left = 0
        right = current_width
        while left < right:
            if height[left] < height[right]:
                area = height[left] * current_width
                left += 1
                if area > max_area:
                    max_area = area
            else:
                area = height[right] * current_width
                right -= 1
                if area > max_area:
                    max_area = area
            current_width -= 1
        return max_area