#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (40.54%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 62.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
# 
# 示例: 
# 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
# 
# 进阶:
# 
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #滑窗法
        start = 0
        end = 0
        min_len = float("inf")
        res=0
        while end<len(nums):
            s-=nums[end]
            end+=1
            while s<=0:
                if end-start<min_len:
                    min_len=end-start
                    res=min_len
                s+=nums[start]
                start+=1
            
        return res


        
# @lc code=end

