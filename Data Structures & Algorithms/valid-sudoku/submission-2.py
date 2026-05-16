class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hs = set()
            for j in range(9):
                c = board[i][j]
                if c !=".":
                    if c in hs:
                        return False
                    else:
                        hs.add(c)
        for i in range(9):
            hs = set()
            for j in range(9):
                c = board[j][i]
                if c !=".":
                    if c in hs:
                        return False
                    else:
                        hs.add(c)
        for i in range(9):
            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            hashset = set()
            for j in range(row_start, row_start+3):
                for k in range(col_start, col_start+3):
                    c = board[j][k]
                    if c !=".":
                        if c in hashset:
                            print(i,j,k,c)
                            return False
                        else:
                            hashset.add(c)
        return True