class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in pairs:
                if not stack or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not len(stack)