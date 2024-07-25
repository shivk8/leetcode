class Solution(object):
    def rec(self, ind, candidates, res, ans):
        ans.append(res[:])
        # loop through possible next
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            res.append(candidates[i])
            self.rec(i + 1, candidates, res, ans)
            res.pop()

    def subset2(self, candidates):
        ans = []
        self.rec(0, sorted(candidates), [], ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subset2([1,2,2]))
