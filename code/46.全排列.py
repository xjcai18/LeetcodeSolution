#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (73.37%)
# Likes:    508
# Dislikes: 0
# Total Accepted:    72.2K
# Total Submissions: 98.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        size=len(nums)
        used=[False for _ in range(size)]
        path=[]
        result=[]
        self.dfs(size,nums,used,0,path,result)
        return result

    def dfs(self,size,nums,used,depth,path,result):
        if len(path)==size:
            result.append(path[:])
        else:
            for i in range(size):
                if not used[i]:#用了一个来记录这个数是否被加入
                    path.append(nums[i])
                    used[i]=True
                    self.dfs(size,nums,used,depth+1,path,result)#这个depth是为了让递归进入下一层
                    used[i]=False#将这个数退回了
                    path.pop()
        
# @lc code=end

