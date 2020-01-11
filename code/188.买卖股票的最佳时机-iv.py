#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (28.25%)
# Likes:    143
# Dislikes: 0
# Total Accepted:    9.2K
# Total Submissions: 32.4K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def help(prices):
            if not prices:
                return 0
            dp=[[0]*2 for _ in range(len(prices))]#定义dp table
            #需要找到一些basic case
            dp[0][0]=0
            dp[0][1]=-prices[0]

            for i in range(1,len(prices)):#转移方程
                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
                dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            return dp[len(prices)-1][0]  

        if not prices:
            return 0
        #dp table
        K=k
        n=len(prices)
        if k>n/2:
            return help(prices)

        dp=[[[0]*2 for _ in range(K+1)] for _ in range(n)]
        #base case

        #状态转移方程
        for i in range(n):
            for k in range(K,0,-1):
                if i==0:                               
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]#这个初始化条件很重要啊
                    continue
                dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return dp[n-1][K][0]#注意代码规范
        
# @lc code=end

