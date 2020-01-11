#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (47.23%)
# Likes:    7310
# Dislikes: 0
# Total Accepted:    757.5K
# Total Submissions: 1.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,value in enumerate(nums):#这里构造了一个哈希表
            hashmap[value]=index
        for i,value in enumerate(nums):
            j=hashmap.get(target-value)#get查询的是键值key，返回的是value
            if j is not None and i != j:
                return [i,j]
        
            
# @lc code=end
