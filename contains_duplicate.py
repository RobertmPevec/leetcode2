class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = set(nums)
        if len(check) < len(nums):
            return True
        else:
            return False