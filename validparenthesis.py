class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}
        for n in s:
            if n in brackets.values():
                # check if n is a opening bracket and if so
                # we push it into the stack
                stack.append(n)
            elif n in brackets:
                if not stack or stack[-1] != brackets[n]:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0