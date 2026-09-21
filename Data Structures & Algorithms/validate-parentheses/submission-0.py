class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in mapping and stack and mapping[c] == stack[-1]:
                stack.pop()
            elif c in mapping.values():
                stack.append(c)
            else:
                return False
        
        #only return True if code finishes with an empty stack
        return not stack