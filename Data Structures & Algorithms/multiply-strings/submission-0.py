class Solution:
    def multiply(self, num1: str, num2: str) -> str:       
        # handles edge case (otherwise 0s get stripped)
        if "0" == num1 or "0" == num2:
            return "0"
        
        # convert strings to numbers
        digits = '0123456789'
        value = {c:i for i, c in enumerate(digits)}

        # reverse numbers to make alg easier
        a = [value[c] for c in reversed(num1)]
        b = [value[c] for c in reversed(num2)]

        # will be reversed actual answer
        res = [0] * (len(a) + len(b))

        for i1 in range(len(a)):
            for i2 in range(len(b)):
                digit = a[i1] * b[i2]
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        
        # answer needs to be unreversed and stripped of leading 0s
        res = res[::-1]
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        res = map(str, res[start: ])
        return "".join(res)