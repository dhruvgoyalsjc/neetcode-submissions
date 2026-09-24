class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # case where line ends
            if length + len(line) + len(words[i]) > maxWidth:
                totalSpaces = maxWidth - length
                spacesPerWord = totalSpaces // max(1, len(line) - 1)
                remainderSpaces = totalSpaces % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spacesPerWord
                    if remainderSpaces:
                        line[j] += " "
                        remainderSpaces -= 1

                res.append("".join(line))
                line, length = [], 0 # resetting line

            # when line doesn't end, just append word to line
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # handle the final line
        finalLine = " ".join(line)
        extraSpaces = maxWidth - len(finalLine)
        res.append(finalLine + " " * extraSpaces)

        return res