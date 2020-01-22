#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.12%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 114.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #dp表还是那个
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]
        print(dp[0])
        if obstacleGrid[0][0]==1:
            return 0
        #初始条件
        dp[0][0]=1
        for i in range(1,n):#如果第一行某一个元素为1则后面的dp元素都是0
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0]=1
        for i in range(1,m):
            if obstacleGrid[0][i]==1:
                break
            else:
                dp[0][i]=1
            

        #转移方程
        for i in range(1,n):
            for j in range(1,m):
                    dp[i][j]=(dp[i-1][j]*abs(obstacleGrid[i-1][j]-1)+dp[i][j-1]*abs(obstacleGrid[i][j-1]-1))*abs(obstacleGrid[i][j]-1)
        print(dp[0])
        return dp[n-1][m-1]
        
# @lc code=end

