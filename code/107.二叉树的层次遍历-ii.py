#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (63.53%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    35.8K
# Total Submissions: 56.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res=[]#讲道理应该是树的深度
        stack=[(0,root)]
        while stack:
            level,node=stack.pop(0)
            if len(res)==level:
                res.append([])
            res[level].append(node.val)
            level+=1#这里表示树的深度
            #每次取出节点level,把他下面的节点存入数组时，加1，算法是没有问题的
            if node.left:
                stack.append((level,node.left))
            if node.right:
                stack.append((level,node.right))
        return res[::-1]
# @lc code=end

