class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I just wanted to try declaring && assigning a 3D list, even if it compromises code readability.
        # rows = [[False] * 9 for _ in range(9)]
        # cols = [[False] * 9 for _ in range(9)]
        # secs = [[False] * 9 for _ in range(9)]
        bundle = [[[False] * 9 for _ in range(9)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if (elm := board[i][j]) == ".": continue
                num = int(elm) - 1
                
                r = j
                c = i
                s = (i // 3) * 3 + (j // 3)

                for idx, k in enumerate([r, c, s]):
                    if bundle[idx][k][num]: return False
                    bundle[idx][k][num] = True

        return True
