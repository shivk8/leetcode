import copy
class Solution(object):
    def rec(self, n, ans, res, row):
        if row == n:
            resCopy = copy.deepcopy(res)
            finRes = ["".join(val) for val in resCopy]
            ans.append(finRes)
            return

        for i in range(0, n):
            if self.canKeep(res, row, i, n):
                res[row][i] = "Q"
                self.rec(n, ans, res, row + 1)
                res[row][i] = "."

    def canKeep(self, res, row, col, n):
        if self.check(res, row, col, n):
            return True
        return False

    def check(self, res, row, col, n):
        dupRow = row
        dupCol = col
        c = 0
        while c < n:
            if res[c][col] == "Q":
                return False
            c+=1

        row = dupRow
        col = dupCol

        while row >= 0 and col >= 0:
            if res[row][col] == "Q":
                return False

            row -= 1
            col -= 1

        row = dupRow
        col = dupCol

        while row < n and col >= 0:
            if res[row][col] == "Q":
                return False
            row += 1
            col -= 1

        row = dupRow
        col = dupCol

        while row >= 0 and col < n:
            if res[row][col] == "Q":
                return False
            row -= 1
            col += 1

        row = dupRow
        col = dupCol

        while row < n and col < n:
            if res[row][col] == "Q":
                return False
            row += 1
            col += 1

        return True

    def solveNQueens(self, n):
        res = []
        for i in range(0, n):
            row = ["." for j in range(0, n)]
            res.append(row)
        ans = []
        self.rec(n, ans, res, 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
