#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#
# https://leetcode-cn.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (51.61%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 14K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，计算整个树的坡度。
# 
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
# 
# 整个树的坡度就是其所有节点的坡度之和。
# 
# 示例:
# 
# 
# 输入: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# 输出: 1
# 解释: 
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 
# 
# 注意:
# 
# 
# 任何子树的结点的和不会超过32位整数的范围。
# 坡度的值不会超过32位整数的范围。
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
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def func(root):
            if root.left is None and root.right is None:
                return root.val
            elif root.left and root.right is None:
                return root.val + func(root.left)
            elif root.right and root.left is None:
                return root.val + func(root.right)
            else:
                return root.val + func(root.left) + func(root.right)

        sum_ = 0
        queue = [root]
        while queue:
            temp = queue.pop()#前后其实没有关系
            if temp.left and temp.right:
                sum_ = sum_ + abs(func(temp.left) - func(temp.right))
                queue.append(temp.left)
                queue.append(temp.right)
            elif temp.left:
                sum_ = sum_ + abs(func(temp.left))
                queue.append(temp.left)
            elif temp.right:
                sum_ = sum_ + abs(func(temp.right))
                queue.append(temp.right)

        return sum_
        
# @lc code=end

