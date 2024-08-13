def isPalindrome(inp):
    revInp = reversed(inp)
    if inp == revInp:
        return True
    return False


class Solution(object):
    def rec(self, board, word,res,c,hashMap,i,j):
        if len(res) == len(word):
            print(res == word)
            return res == word
        if i >= len(board) or j >= len(board[0]):
            if res != word:
                return False

        if self.isValid(hashMap,word,res,i-1,j,c) or self.isValid(hashMap,word,res,i+1,j,c) or self.isValid(hashMap,word,res,i,j-1,c) or self.isValid(hashMap,word,res,i,j+1,c):
                    pass
        else:
            res[::-1]
    def isValid(self,hashMap,word,res,row,col,c):
        if hashMap[row][col] == -1:
            hashMap[row][col] = 1
            res = res + word[c]
            return True
        return False

    def exist(self, word, board, res):
        hashMap = []
        c = 0
        for i in range(0, len(board)):
            row = [-1 for j in range(0, len(board[0]))]
            hashMap.append(row)
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == word[c]:
                    val = self.rec(board, word, res, c, hashMap,i,j)
                    c = c+1
                    if val is not None:
                        return val


if __name__ == "__main__":
    s = Solution()
    res = ""
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(s.exist(word, board, res))
