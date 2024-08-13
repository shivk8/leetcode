from collections import defaultdict
class Solution(object):

    def longestSubArray(self, arr,k,n):
        hashMap = defaultdict()
        sumL = 0
        lenL = 0
        maxL = -9999
        for i in range(0,n):
            sumL += arr[i]
            if sumL not in hashMap.keys():
                hashMap[sumL] = i

            if sumL == k:
                maxL = max(maxL,i+1)

            #check if subarray needs to sum upto k, is there subarray with sum x-k
            if (sumL-k) in hashMap.keys():
                key = sumL - k
                val = hashMap[key]
                lenL = i - val
                maxL = max(maxL, lenL)

        return maxL






if __name__ == "__main__":
    s = Solution()
    print(s.longestSubArray([13, 0 ,6 ,15, 16, 2 ,15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6],15,17))
