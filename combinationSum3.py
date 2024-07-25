class Solution(object):
    def rec(self, ind, candidates, res, k,n,ans):
        if len(res) == k:
            if n == 0:
                ans.append(res[:])
            return

        # loop through possible next
        for i in range(ind, len(candidates)):
            if candidates[ind] > n:
                break
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            res.append(candidates[i])
            self.rec(i + 1, candidates, res,k,n - candidates[i], ans)
            res.pop()

    def combinationSum3(self, candidates,k,n):
        ans = []
        self.rec(0, candidates, [], k,n,ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3([1,2,3,4,5,6,7,8,9],4,1))
