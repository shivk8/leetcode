from collections import defaultdict
import copy
class Solution(object):
    def rec(self,row,col,board,rows,cols,squares,res,ans):
        if row == len(board):
            ans = copy.deepcopy(res)
            print(ans)
            return

        if res[row][col] == ".":
            for i in range(1, 5):
                if str(i) not in rows[row] and str(i) not in cols[col] and str(i) not in squares[(row//2),(col//2)]:
                    res[row][col] = str(i)
                    rows[row].add(str(i))
                    cols[col].add(str(i))
                    squares[(row//2),(col//2)].add(str(i))
                if col == len(board[0]) - 1:
                    self.rec(row + 1, 0, board, rows, cols, squares, res, ans)
                else:
                    self.rec(row, col + 1, board, rows, cols, squares, res, ans)
        else:
            if col == len(board[0]) - 1:
                self.rec(row + 1, 0, board, rows, cols, squares, res, ans)
            else:
                self.rec(row, col + 1, board, rows, cols, squares, res, ans)



            # res[row][col] = "."
            # rows[row].pop()
            # cols[col].pop()
            # squares[(row // 3), (col // 3)].pop()



    def sudoKuSolver(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        res = board[:][:]
        ans = []
        for i in range(0, len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                if board[i][j] not in cols[j]:
                    cols[j].add(board[i][j])
                if board[i][j] not in squares[(i//2),(j//2)]:
                    squares[(i//2),(j//2)].add(board[i][j])

        self.rec(0,0,board,rows,cols,squares,res,ans)

        return ans


if __name__ == "__main__":
    s = Solution()
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board = [["1",".",".","4"],
             ["3",".",".","2"],
             [".","1","4","."],
             [".","3",".","1"]]
    print(s.sudoKuSolver(board))
