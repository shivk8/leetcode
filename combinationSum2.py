class Solution(object):
    def rec(self, ind, target, candidates, finalRes, res):
        if target == 0:
            if sorted(res) not in finalRes:
                finalRes.append(sorted(res[:]))
            return

        if ind == 0:
            if candidates[ind] == target:
                res.append(candidates[ind])
                if sorted(res) not in finalRes:
                    finalRes.append(sorted(res[:]))
            return

        if target >= candidates[ind]:
            res.append(candidates[ind])
            self.rec(ind - 1, target - candidates[ind], candidates, finalRes, res)
            res.pop()
        self.rec(ind - 1, target, candidates, finalRes, res)
        return

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        finalRes = []
        self.rec(len(candidates) - 1, target, candidates, finalRes, [])
        return finalRes

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],30))