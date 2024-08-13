def isPalindrome(inp):
    revInp = reversed(inp)
    if inp == revInp:
        return True
    return False


class Solution(object):
    def rec(self, ind, inputStr, res, ans,n):
        if ind == n:
            ans.append(res[:])
            return

        # loop through possible next
        for i in range(ind, n):
            subStr1 = inputStr[ind:1+i]
            flag = self.isPalindrome(subStr1)
            if flag:
                print(subStr1)
                res.append(subStr1)
                self.rec(i + 1, inputStr, res, ans, n)
                res.pop()
        return

    def isPalindrome(self, inp):
        rev = inp[::-1]
        if inp == rev:
            return True
        return False
    def partition(self, inputStr):
        ans = []
        self.rec(0, inputStr, [], ans,len(inputStr))
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aabb"))
