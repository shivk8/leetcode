class Solution(object):
    def recSubsetPresent(self,n, k, a, s, ind):
        if ind == n:
            if sum(s) == k:
                return True
            return False
        s.append(a[ind])
        take = self.recSubsetPresent(n, k, a, s, ind + 1)
        if take:
            return take
        s.pop()
        not_take = self.recSubsetPresent(n, k, a, s, ind + 1)
        if not_take:
            return True
        return False

    def isSubsetPresent(self, n, k, a,ind) -> bool:
        subSet = []
        return self.recSubsetPresent(n, k, a, subSet, 0)

if __name__ == "__main__":
    s = Solution()
    print(s.isSubsetPresent(5,14,[4,2,5,6,7],[]))