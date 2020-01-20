#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.54%)
# Likes:    398
# Dislikes: 0
# Total Accepted:    43.3K
# Total Submissions: 99.2K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        '''
        dp=[1]
        for i in range(1,len(nums)):
            dp.append(1)
            for j in range(i):#这里以下是转移方程，怎么想到的呢，一般来讲是dp[i]
                #和dp[i-1]或者及其以前的一个状态之间的关系
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)#这一步其实是求之前的dp[e]+1 for e in (0,i)的最大值
        return max(dp)
        '''

                    
# @lc code=end

