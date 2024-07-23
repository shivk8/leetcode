class Solution(object):
    def rec(self, arr, n, res, ind,ans):
        if ind == n:
            ans.append(sum(res[:]))
            return

        res.append(arr[ind])
        take = self.rec(arr, n, res, ind + 1,ans)
        res.pop()

        notTake = self.rec(arr, n, res, ind + 1,ans)

        return

    def subsetSum1(self, arr, n):
        # code here
        ans = []
        self.rec(arr, n, [], 0,ans)
        print(ans)

if __name__ == "__main__":
    s = Solution()
    s.subsetSum1([2,3],2)
