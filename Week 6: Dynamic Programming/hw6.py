# Leetcode 518. Coin Change 2
'''
Runtime: 196 ms, faster than 65.04% of Python3 online submissions for Coin Change 2.
Memory Usage: 13.3 MB, less than 42.70% of Python3 online submissions for Coin Change 2.
'''
class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[-1]
    





# Leetcode 63. Unique Paths II
'''
Runtime: 32 ms, faster than 96.19% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.2 MB, less than 44.20% of Python3 online submissions for Unique Paths II.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for col in range(n)] for row in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    if i:
                        dp[i][j] = dp[i-1][j]
                    elif j:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# Leetcode 64. Minimum Path Sum

'''
Runtime: 48 ms, faster than 93.24% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 14.4 MB, less than 78.35% of Python3 online submissions for Minimum Path Sum.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                    
        return grid[-1][-1]
        
# Leetcode 5. Longest Palindromic Substring

'''
Runtime: 2100 ms, faster than 45.03% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 21.1 MB, less than 13.88% of Python3 online submissions for Longest Palindromic Substring.
'''
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        n = len(s)
        ans = '' 
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            max_len = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
                
        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        ans = s[i:j+1]
        return ans
