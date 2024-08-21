
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        profit = 0
        maxProfit = 0
        minPrice = prices[0]

        for i in range(1,n):
            minPrice = min(minPrice,prices[i-1])
            profit = nums[i] - minPrice
            if profit < 0:
                profit = 0
            maxProfit = max(profit,maxProfit)

        return maxProfit









if __name__ == "__main__":
    s = Solution()
    nums = [7,1,5,3,6,4]
    print(s.maxProfit(nums))
