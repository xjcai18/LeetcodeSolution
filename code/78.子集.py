#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (75.79%)
# Likes:    448
# Dislikes: 0
# Total Accepted:    56.3K
# Total Submissions: 73.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        size=len(nums)
        self.backtracking(nums,0,size,path,result)
        return result

    def backtracking(self,nums,start,size,path,result):
    #中止条件是什么呢，包含不同元素
        result.append(path[:])#记录回溯的所有过程
        for i in range(start,size):

            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtracking(nums,i+1,size,path,result)
            path.pop()
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        size=len(nums)
        for i in range(size+1)
            self.backtracking(nums,0,size,path,result,i)#循环遍历所有的
        return result

    def backtracking(self,nums,start,size,path,result,length):#增加一个参数length来表示层数，代码就和之前的一样了
    #中止条件是什么呢，包含不同元素
        if len(path)==length:
            result.append(path[:])
        for i in range(start,size):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtracking(nums,i+1,size,path,result,length)
            path.pop()

        
# @lc code=end

