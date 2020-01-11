#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (71.64%)
# Likes:    421
# Dislikes: 0
# Total Accepted:    108.6K
# Total Submissions: 151.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
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

    def maxDepth(self, root: TreeNode) -> int:
        #迭代BFS遍历
        if root is None:
            return 0
        stack=[(1,root)]
        while stack:
            depth,node=stack.pop(0)
            max_depth=depth
            depth+=1
            if node.left:
                stack.append((depth,node.left))
            if node.right:
                stack.append((depth,node.right))
        return max_depth #因为是BFS，所以最后一个节点得深度就是我们需要得最大得
# @lc code=end

