class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        num_to_alphabet = [chr(c) for c in range(ord("z"), ord("a") - 1, -1)]

        result = list()
        for w in words:
            tmp = 0
            for c in w: tmp += weights[ord(c) - 97]
            result.append(num_to_alphabet[tmp % 26])

        return "".join(result)
