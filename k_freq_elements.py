class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = {}
        for num in nums:
            if num not in ret:
                ret[num] = 1
            else:
                ret[num] += 1
        sorted_frequencies = sorted(ret.items(), key=lambda x: x[1], reverse=True)
        final_list = []
        for i in range(k):
            final_list.append(sorted_frequencies[i][0])
        return final_list