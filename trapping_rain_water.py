# optimal O(n) solution with O(1) memory
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        in1 = 0
        in2 = len(height) - 1
        squares = 0
        maxL = height[in1]
        maxR = height[in2]
        while in1 < in2:
            if maxL < maxR:
                in1 += 1
                if height[in1] < maxL:
                    squares += maxL - height[in1]
                if maxL < height[in1]:
                    maxL = height[in1]
            else:
                in2 -= 1
                if height[in2] < maxR:
                    squares += maxR - height[in2]
                if maxR < height[in2]:
                    maxR = height[in2]
        return squares