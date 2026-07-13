class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = list()
        temp = list()
        counter = 0

        for w in words:
            n = len(w)

            if counter + len(temp) + n > maxWidth:
                margin = maxWidth - counter
                spacings = len(temp) - 1

                if spacings:
                    q = margin // spacings
                    r = margin % spacings

                    s = [q] * spacings
                    s[0:r] = [i + 1 for i in s[0:r]]

                    concat = ""
                    for i in range(spacings):
                        concat += temp[i]
                        concat += (" " * s[i])
                    concat += temp[-1]
                else:
                    concat = ""
                    concat += temp[0]
                    concat += (" " * (margin))

                result.append(concat)

                counter = 0
                temp = list()
            
            counter += n
            temp.append(w)

        concat = ""
        counter = 0
        for w in temp[:-1]:
            counter += len(w) + 1
            concat += w
            concat += " "
        counter += len(temp[-1])
        concat += temp[-1]

        concat += " " * (maxWidth - counter)

        result.append(concat)
        
        return result
            
            