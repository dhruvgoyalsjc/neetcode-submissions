class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in mapping: 
                if stack and mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        #only return True if code finishes with an empty stack
        return not stack