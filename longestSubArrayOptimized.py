
class Solution(object):

    def longestSubArray(self, arr,k,n):
        p1, p2 = 0, 0
        sumL = arr[0]
        maxL = -9999
        while p2 < n:
            while sumL > k and p1 <= p2:
                sumL -= arr[p1]
                p1 += 1

            if sumL == k:
                maxL = max(maxL, p2-p1+1)

            p2 += 1
            if p2 < n:
                sumL += arr[p2]
        return maxL

if __name__ == "__main__":
    s = Solution()
    print(s.longestSubArray([1, -1, 1],1,3))
