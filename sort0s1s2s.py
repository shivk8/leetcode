
class Solution(object):

    def sortColors(self, nums):
        n = len(nums)
        low = 0
        mid = 0
        high = n-1

        while mid <= high:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                high -= 1

if __name__ == "__main__":
    s = Solution()
    nums = [2,0,1]
    s.sortColors(nums)
    print(nums)
