class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for i in n:
                count[ord(i) - ord("a")] += 1
            result[tuple(count)].append(n)
        return result.values()