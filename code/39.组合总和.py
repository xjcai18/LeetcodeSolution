#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (67.76%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    58.4K
# Total Submissions: 85.7K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size=len(candidates)
        if size==0:#特例
            return []
        candidates.sort()#排序
        path=[]#在遍历的时候记录路劲，一般来说是个栈
        res=[]#存放结果
        self.dfs(candidates,0,size,path,res,target)

        return res
    def dfs(self,candidates,begin,size,path,res,target):
        #先写递归的中止条件 target==0
        if target==0:
            res.append(path[:])#注意这里为什么要这么写

        for index in range(begin,size):
            residue=target-candidates[index]
            #剪枝操作，如果不满足接下来的递归不用进行
            if residue<0:
                break
            path.append(candidates[index])
            self.dfs(candidates,index,size,path,res,residue)
            path.pop()#回溯法最后都要回删，但是为什么？？？？



        
# @lc code=end

