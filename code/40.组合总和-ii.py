#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (59.07%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 61.5K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            if path not in res:
                res.append(path[:])#注意这里为什么要这么写

        for index in range(begin,size):
            residue=target-candidates[index]
            #剪枝操作，如果不满足接下来的递归不用进行
            if residue<0:
                break
            path.append(candidates[index])
            self.dfs(candidates,index+1,size,path,res,residue)
            path.pop()#回溯法最后都要回删，但是为什么？？？？
        
# @lc code=end

