#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (59.13%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 13.9K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 
# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 
# 返回获得利润的最大值。
# 
# 示例 1:
# 
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 注意:
# 
# 
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        dp=[[0]*2 for _ in range(len(prices))]#定义dp table
        #需要找到一些basic case


        for i in range(len(prices)):#转移方程
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)#相当于卖出股票的价格贬低了了
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])#也可以写在这一行，相当于买入的价格增加了
        return dp[len(prices)-1][0]
        
# @lc code=end

