def isPalindrome(inp):
    revInp = reversed(inp)
    if inp == revInp:
        return True
    return False


class Solution(object):
    def rec(self, ind, prevStr, inputStr, res,n,wordDict):
        if ind == n:
            print(res)
            for word in res:
                if word not in wordDict:
                    return False
            return True

        prevStr = prevStr + inputStr[ind:1+ind]
        #print(prevStr)
        if ind + 1 != n:
            if prevStr in wordDict:
                if (prevStr + inputStr[ind + 1] not in wordDict):
                    res.append(prevStr)
                    prevStr = ""
        else:
            res.append(prevStr)
        return self.rec(ind + 1, prevStr, inputStr, res, n,wordDict)

    def wordBreak(self, inputStr,wordDict):
        prevStr = ""
        return self.rec(0, prevStr, inputStr, [],len(inputStr),wordDict)

if __name__ == "__main__":
    s = Solution()
    #wordDict = ["cats","dog","sand","and","cat"]
    #wordDict = ["leet","code"]
    # wordDict = ["apple", "pen"]
    wordDict = ["car", "ca","rs"]
    #wordDict = ["aaaa", "aaa"]
    print(s.wordBreak("cars",wordDict))
