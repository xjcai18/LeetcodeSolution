#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (51.78%)
# Likes:    676
# Dislikes: 0
# Total Accepted:    111K
# Total Submissions: 214.2K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 
# 注意你不能在买入股票前卖出股票。
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """       
        if not prices:
            return 0
        dp=[[0]*2 for _ in range(len(prices))]#定义dp table
        #需要找到一些basic case
        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1,len(prices)):#转移方程
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],-prices[i])#思考一下这里为什么要用，
            #因为只可以交易一次但是怎么去理解
        return dp[len(prices)-1][0]
        """
        n = len(prices)
        if n==0:
            return 0

        # 初始化 buying_prices、selling_prices
        buying_prices = prices.copy()
        selling_prices = prices.copy()
        
        # 计算每一天的最优买入价
        buying_price = prices[0]
        for i in range(n):
            if buying_price > prices[i]:
                buying_price = prices[i]
            buying_prices[i] = buying_price
            
        # 计算每一天可操作的最高卖出价
        selling_price = prices[n-1]
        for i in range(n-1,-1,-1):
            if selling_price < prices[i]:
                selling_price = prices[i]
            selling_prices[i] = selling_price
            
        max_profit = max([y - x for x, y in zip(buying_prices,selling_prices)])
        return max(max_profit, 0)



        
# @lc code=end

