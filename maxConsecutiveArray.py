class Solution(object):

    def maxConsecutive1s(self, a1):
        n1 = len(a1)

        if n1 == 0:
            return 0
        maxLen = -1
        recLen = -1

        for i in range(0,n1):
            if a1[i] == 1:
                recLen += 1
                if recLen > maxLen:
                    maxLen = recLen

            if a1[i] != 1:
                recLen = 0

        return maxLen






if __name__ == "__main__":
    s = Solution()
    print(s.maxConsecutive1s([1,1,0,0,1,0,1,1,1,0,1,1,1,]))
