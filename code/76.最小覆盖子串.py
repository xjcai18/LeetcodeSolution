#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.77%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    22K
# Total Submissions: 62.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #滑动窗口法
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res=""
        for i in t:
            lookup[i]+=1
        while end < len(s):
            if lookup[s[end]]>0:
                counter-=1
            lookup[s[end]]-=1#在t和其他的元素相区别
            end+=1
            while counter==0:
                if min_len>end-start:
                    min_len=end-start
                    res=s[start:end]
                if lookup[s[start]]==0:
                    counter+=1
                lookup[s[start]]+=1
                start+=1
        return res

        
# @lc code=end

