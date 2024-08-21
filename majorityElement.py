
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        cnt = 0
        i = 0

        while i <= n-1:
            if cnt == 0:
                ele = nums[i]
                cnt += 1
                i += 1
            elif nums[i] == ele:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                i += 1

        majority = len(nums)/2
        cnt = 0

        for i in range(0,n):
            if nums[i] == ele:
                cnt += 1

        if cnt > majority:
            return ele



if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))
