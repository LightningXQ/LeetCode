class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        dct = dict()
        val = 0
        for c in range(ord("z"), ord("a") - 1, -1):
            dct[val] = chr(c)
            val += 1

        result = list()
        for w in words:
            tmp = 0
            for c in w: tmp += weights[ord(c) - 97]
            result.append(dct[tmp % 26])

        return "".join(result)
    