#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.96%)
# Likes:    1642
# Dislikes: 0
# Total Accepted:    168.2K
# Total Submissions: 598.1K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        #动态规划，返回j-i+1最大的值
        n=len(s)
        dp=[[0]*n for _ in range(n)]#定义为s[i:j]是否为回文子串
        res=""
        #初始条件
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j]= s[i]==s[j] and (j-i<2 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 >len(res):
                    res=s[i:j+1]
        return res
        '''
        return self.spread_from_center(s)
 #中心扩散法Spread From Center
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
   

# 动态规划法-中心扩散法Spread From Center
    def spread_from_center(self, s:str) -> str:
        
        if s==s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd= self.spread(s,i, i)
            palindrome_even= self.spread(s,i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd,palindrome_even,res,key=len)
        return res



                

        



        
# @lc code=end

