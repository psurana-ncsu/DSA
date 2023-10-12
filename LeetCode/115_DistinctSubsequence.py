class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)] 
        
        # Base case
        for j in range(N + 1):
            dp[0][j] = 0
        
        # Base case
        for i in range(M + 1):
            dp[i][0] = 1
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j]

                # If the characters match, we add the result
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
            
        return dp[M][N]

