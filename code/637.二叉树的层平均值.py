#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (62.05%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 18.5K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
# 
# 示例 1:
# 
# 输入:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 
# 
# 注意：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        res=[]
        count=[]
        stack=[(0,root)]
        while stack:
            level,node=stack.pop()#注意这里从前取，从后取意义不大，因为标注了层次，而且我们要的是统计信息求和，顺序不重要
            if len(res)==level:
                res.append(0)
                count.append(0)
            res[level]=res[level]+node.val
            count[level]+=1
            level+=1
            if node.left:
                stack.append((level,node.left))
            if node.right:
                stack.append((level,node.right))
        for i in range(len(res)):
                res[i]=res[i]/count[i]
        return res
            
# @lc code=end

