class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while (i < len(words)):
            # can't add next word case
            if length + len(line) + len(words[i]) > maxWidth:
                total_space = maxWidth - length
                space_per = total_space // max(1, len(line) - 1)
                remainder = total_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * space_per
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))
                line, length = [], 0 # reset line and length

            # can add word case
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # add final line
        final_line = " ".join(line)
        remaining = maxWidth - len(final_line)
        res.append(final_line + " " * remaining)

        return res