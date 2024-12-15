class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        min_length = len(strs[0])
        cur = 0
        for n in range(1, len(strs)):
            if len(strs[n]) < len(min_length):
                min_length = strs[n]
        for j in range(min_length):
            current_character = strs[0][j]
            for i in strs[1:]:
                if strs[i][cur] != current_character:
                    return output
            cur += 1
            output += current_character
        return output
