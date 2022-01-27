class Solution:
    def solveNQueens(self, n):
        #assigning to set to have only unique numbers
        col = set()#will store unique columns
        #posDiag is achieved by (r+c), for example (3,0)=(3+0) = 3 (2,1)=(2+1)=3
        posDiag = set()#will store unique posDiagonal
        #negDiag is achieved by (r-c), for example (0,0)=(0-0) = 0 (1,1)=(1-1)=0
        negDiag = set()#will store unique negDiag

        res = []#will store the result
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            if r == n:#if the last row has been reached 
                copy = ["".join(row) for row in board]#iterating through the modified board
                res.append(copy)#appending each of the solutions
                return 
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:#checking if already present
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)
                #if the current position is not possible, backtrack
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return res#returning result

s = Solution()
print(s.solveNQueens(4))