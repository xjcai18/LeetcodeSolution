#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.11%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    67.4K
# Total Submissions: 112.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 

# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#题目的前提是比较熟练的层次遍历树
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        if root is None:
            return []
        res=[]#讲道理应该是树的深度
        stack=[(0,root)]
        level=0
        while stack:
            
            res.append([])
            level,node=stack.pop(0)
            res[level].append(node.val)
            level+=1#这里表示树的深度
            #每次取出节点level,把他下面的节点存入数组时，加1，算法是没有问题的
            if node.left:
                stack.append((level,node.left))
            if node.right:
                stack.append((level,node.right))
        return res[:level]
        '''

        res=[]
        def help(root,level):
            if root is None:
                return []
            if len(res)==level:
                res.append([])
            res[level].append(root.val)
            help(root.left,level+1)
            help(root.right,level+1)
        help(root,0)   
        return res

       
# @lc code=end

