#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (56.29%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    35.6K
# Total Submissions: 62.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        size=len(nums)
        used=[False for _ in range(size)]
        path=[]
        result=[]
        self.dfs(size,nums,used,0,path,result)
        return result

    def dfs(self,size,nums,used,depth,path,result):
        if len(path)==size and path not in result:
            result.append(path[:])
        elif len(path)==size:
            return 
        else:
            for i in range(size):
                if not used[i]:#用了一个来记录这个数是否被加入
                    path.append(nums[i])
                    used[i]=True
                    self.dfs(size,nums,used,depth+1,path,result)#这个depth是为了让递归进入下一层
                    used[i]=False#将这个数退回了
                    path.pop()
        
# @lc code=end

