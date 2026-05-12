class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for i, row in enumerate(boxGrid):
            row = "".join(row).split('*')
            new_row = list()

            for substr in row:
                count = substr.count('#')
                new_row.extend(['.'] * (len(substr) - count) + ['#'] * count + ['*'])

            new_row.pop()   # detach last '*'
            boxGrid[i] = new_row

        result = [list(row) for row in zip(*boxGrid[::-1])]

        return result
