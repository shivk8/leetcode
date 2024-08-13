class Solution(object):

    def intersectionArray(self, a1, a2):
        n1 = len(a1)
        n2 = len(a2)

        if n1 == 0 or n2 == 0:
            return []

        res = []
        i, j = 0, 0

        while i < n1 and j < n2:
            if a2[j] < a1[i]:
                j += 1

            if a1[i] < a2[j]:
                i += 1

            if a1[i] == a2[j]:
                res.append(a1[i])
                i+=1
                j+=1
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.intersectionArray([2,2,2,3,3,4,5,6],[2,3,3,5,6,6,7]))
