#solution in n^2

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for n in nums:
            sumofbefore = 1
            sumofafter = 1
            index = nums.index(n)
            for j in nums[:index]:
                sumofbefore *= j
            for k in nums[index + 1:]:
                sumofafter *= k
            output.append(sumofbefore * sumofafter)
        return output

# optimal o(n) solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res