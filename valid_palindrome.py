#O(n)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = s.lower().strip()[::-1]
        ns = re.sub(r'[^a-z0-9]', '', ns)
        s = s.lower().strip()
        s = re.sub(r'[^a-z0-9]', '', s)        
        return ns == s
# better memory:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            while left < right and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True