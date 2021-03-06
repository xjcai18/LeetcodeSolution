#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (63.75%)
# Likes:    366
# Dislikes: 0
# Total Accepted:    52.8K
# Total Submissions: 82.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #定义一个dp table
        n=len(grid)
        m=len(grid[0])
        dp=[[0]*m for _ in range(n)]

        #初始条件
        dp[0][0]=grid[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        #转移方程
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[n-1][m-1]





            



        
# @lc code=end

