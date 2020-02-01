#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (69.50%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 18.3K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        path=[]
        result=[]
        self.dfs(k,n,1,path,result)
        return result


    def dfs(self,k,n,start,path,result):
        if k==0 and n==0:
            result.append(path[:])
        elif k==0:
            return 
        elif n==0:
            return 
        for i in range(start,10):
            residue=n-i
            if residue<0:#剪枝操作
                break
            path.append(i)
            self.dfs(k-1,residue,i+1,path,result)
            path.pop()


        
# @lc code=end

