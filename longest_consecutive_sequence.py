# O(n log n) time complexity:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        maxi = 1
        current_streak = 1
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i] + 1:
                current_streak += 1
                if current_streak > maxi:
                    maxi = current_streak
            else:
                current_streak = 1
        return maxi
            
# O(n) time complexity:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        maxi = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                if current_streak > maxi:
                    maxi = current_streak
        return maxi