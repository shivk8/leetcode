class Solution(object):
    def rec(self, arr,visited,res,ans):
        if len(res) == len(visited):
                ans.append(res[:])
                return

        for i in range(0,len(arr)):
            if visited[i] == 0:
                visited[i]=1
                res.append(arr[i])
                self.rec(arr,visited,res,ans)
                res.pop()
                visited[i] = 0

    def permutaions(self, arr):
        ans = []
        visited = [0 for i in range(0,len(arr))]
        self.rec(arr,visited, [],ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.permutaions([1,2,3,4]))
