#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (51.10%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    14.3K
# Total Submissions: 27.7K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        #其实就是找出现奇数次的
        n=len(s)
        dic={}
        for value in s:
            if value in dic:
                dic[value]+=1
            else:
                dic[value]=1
        odd=0
        for k, v in dic.items():
            if v%2==1:
                odd+=1
        if odd>=1:
            n=n+1-odd
        return n
        
# @lc code=end

