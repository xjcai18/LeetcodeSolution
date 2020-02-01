#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (58.10%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    20.2K
# Total Submissions: 34.6K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        nums.sort()
        size=len(nums)
        self.backtracking(nums,0,size,path,result)
        return result

    def backtracking(self,nums,start,size,path,result):
    #中止条件是什么呢，包含不同元素
        if path not in result:
            result.append(path[:])
        for i in range(start,size):   

            path.append(nums[i])
            self.backtracking(nums,i+1,size,path,result)
            path.pop()
        
# @lc code=end

