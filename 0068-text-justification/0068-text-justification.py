class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = list()
        line = list()
        len_count = 0
        word_count = 0
        char_count = 0

        for w in words:
            prev_width = char_count + word_count - 1
            curr_width = char_count + word_count + len(w)

            if curr_width > maxWidth:
                margin = maxWidth - char_count
                spacings = word_count - 1

                if spacings:
                    base = margin // spacings
                    offset = margin % spacings

                    spaces = [base] * spacings
                    spaces[0:offset] = [i + 1 for i in spaces[0:offset]]

                    string = ""
                    for word, space in zip(line, spaces):
                        string += word
                        string += " " * space
                    string += line[-1]
                else:
                    string = ""
                    string += line[0]
                    string += " " * margin

                result.append(string)

                char_count = word_count = 0
                line = list()
            
            char_count += len(w)
            word_count += 1
            line.append(w)

        string = ""
        for w in line[:-1]:
            string += w
            string += " "
        string += line[-1]

        count = char_count + word_count - 1
        string += " " * (maxWidth - count)

        result.append(string)
        
        return result
            
            