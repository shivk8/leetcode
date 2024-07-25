class Solution(object):
    def rec(self, ind, digitsArr, res, ans,n):
        if len(res) == n:
                if len(res) == 0:
                    return
                resStr = "".join(res)
                ans.append(resStr)
                return

        for i in range(0,len(digitsArr[ind])):
            res.append(digitsArr[ind][i])
            self.rec(ind+1,digitsArr,res,ans,n)
            res.pop()

    def letterCombinations(self, digits):
        ans = []
        digits2alp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                      "7":"pqrs","8":"tuv","9":"wxyz"}
        digitsArr = [digits2alp[ind] for ind in digits]
        self.rec(0, digitsArr, [], ans,len(digitsArr))
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
