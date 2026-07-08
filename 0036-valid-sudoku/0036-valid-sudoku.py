class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        secs = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".": continue
                
                r = j
                c = i
                s = (i // 3) * 3 + (j // 3)

                if num in rows[r] or num in cols[c] or num in secs[s]: 
                    return False

                rows[r].add(num)
                cols[c].add(num)
                secs[s].add(num)

        return True