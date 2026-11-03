class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else: # "/" case
                    result = int(a / b)

                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]