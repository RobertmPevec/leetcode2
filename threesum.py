# O(n^2) solution:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = []
        nums.sort()
        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            left =  n + 1
            right = len(nums) - 1
            while left < right:
                temp_value = nums[n] + nums[left] + nums[right]
                if temp_value == 0:
                    solutions.append([nums[n],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif temp_value < 0:
                    left += 1
                else:
                    right -= 1
        return solutions