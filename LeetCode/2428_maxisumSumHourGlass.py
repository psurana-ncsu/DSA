class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        m,n = len(grid), len(grid[0])
        for i in range(1, m-1):
            for j in range(1, n-1):
                curr = grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]+grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]+grid[i][j]
                ans = max(ans, curr)
        return ans

        
