class Solution(object):
    def f(self, ind, res, nums):
        if ind >= len(nums):
            return [res[:]]
        res.append(nums[ind])
        take = self.f(ind + 1, res, nums)
        res.remove(nums[ind])
        notTake = self.f(ind + 1, res, nums)
        return take + notTake

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.f(0, [], nums)


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))