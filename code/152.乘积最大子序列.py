#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (36.40%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 85.5K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
'''
        imax=1#维护一个最大值
        imin=1#维护一个最小值，因为可能为负负得正
        res=float("-inf")
        for value in nums:
            if value<0:#如果后一个数为负，交换最大值和最小值
                imax,imin=imin,imax
            imax=max(imax*value,value)
            imin=min(imin*value,value)

            res=max(res,imax)
        return res
        '''

        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)




# @lc code=end

