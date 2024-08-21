
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxSum = -99999
        sumI = 0

        #optimal solution - kadane's algorithm
        for i in range(0,n):
            if sumI < 0:
                sumI = 0
            sumI += nums[i]

            if sumI > maxSum:
                maxSum = sumI

        return maxSum





if __name__ == "__main__":
    s = Solution()
    nums = [-4,-2,3,-1]
    print(s.maxSubArray(nums))
