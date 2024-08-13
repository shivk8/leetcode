import copy
class Solution(object):
    def rec(self, n, ans, res, row, lowerDiagonal,upperDiagonal,sameCol):
        if row == n:
            resCopy = copy.deepcopy(res)
            finRes = ["".join(val) for val in resCopy]
            ans.append(finRes)
            return

        for i in range(0, n):
            if sameCol[i] == 0 and lowerDiagonal[row+i] == 0 and upperDiagonal[(i-row)+n-1] == 0:
                lowerDiagonal[row + i] = 1
                upperDiagonal[(i - row) + n - 1] = 1
                sameCol[i] = 1
                res[row][i] = "Q"
                self.rec(n, ans, res, row + 1, lowerDiagonal,upperDiagonal,sameCol)
                res[row][i] = "."
                lowerDiagonal[row + i] = 0
                upperDiagonal[(i - row) + n - 1] = 0
                sameCol[i] = 0


    def solveNQueens(self, n):
        res = []
        for i in range(0, n):
            row = ["." for j in range(0, n)]
            res.append(row)
        ans = []
        sameCol = [0 for i in range(0,n)]
        lowerDiagonal = [0 for i in range(0,2*n)]
        upperDiagonal = [0 for i in range(0,2*n)]
        self.rec(n, ans, res, 0, lowerDiagonal,upperDiagonal,sameCol)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
