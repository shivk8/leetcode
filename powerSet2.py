class Solution(object):

    def powerSet(self, candidates, n):
        ans = []
        for num in range(0,(1<<n)-1):
            subset = []
            for i in range(0,n):
                if (num & (1<<i)) != 0:
                    subset.append(int(candidates[i]))

            print(subset)
            ans.append(sum(subset))

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.powerSet([1,2,3],3))
