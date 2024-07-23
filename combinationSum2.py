class Solution(object):
    def rec(self, ind, target, candidates, res, ans):
        if target == 0:
            ans.append(res[:])

        # loop through possible next
        for i in range(ind, len(candidates)):
            if candidates[ind] > target:
                break
            if i > ind and candidates[ind] == candidates[ind - 1]:
                continue
            res.append(candidates[i])
            self.rec(i + 1, target - candidates[i], candidates, res, ans)
            res.pop()

        return

    def powerSet(self, candidates, target):
        ans = []
        self.rec(0, target, sorted(candidates), [], ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([2,5,2,1,2],5))
