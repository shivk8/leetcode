class Solution(object):
    def recSubsetPresent(self,n, k, a, s, ind):
        if ind == n:
            if sum(s) == k:
                return [s[:]]
            return None
        s.append(a[ind])
        take = self.recSubsetPresent(n, k, a, s, ind + 1)
        s.pop()
        not_take = self.recSubsetPresent(n, k, a, s, ind + 1)

        res = []
        if take is not None and not_take is not None:
            return take + not_take
        if not_take is None:
            if take is None:
                return None
            return take
        return not_take

    def isSubsetPresent(self, n, k, a,ind) -> bool:
        subSet = []
        res = self.recSubsetPresent(n, k, a, subSet, 0)
        print(set(res))

if __name__ == "__main__":
    s = Solution()
    s.isSubsetPresent(5,14,[2,3,5,7,7],[])