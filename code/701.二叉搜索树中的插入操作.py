#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#
# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (70.87%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 9.5K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
# 
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
# 
# 例如, 
# 
# 
# 给定二叉搜索树:
# 
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# 和 插入的值: 5
# 
# 
# 你可以返回这个二叉搜索树:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# 或者这个树也是有效的:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        if root is None:
            return TreeNode(val)
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val)
        else:
            root.left=self.insertIntoBST(root.left,val)
        return root
        '''
        #寻找父节点，然后直接放在该父节点的子节点即可
        if root is None:
            return TreeNode(val)
        cur=root
        parent=cur
        while cur is not None: #什么时候遍历中止，当子节点为空是，得到该子节点的父节点
            cmp=val-cur.val
            parent=cur
            if cmp <0 :#如果这个数比根节点小，则他的父节点应该在左边或者就是根节点
                cur=cur.left
            elif cmp>0:
                cur=cur.right
            else:
                return root #如果相等不用任何改变
        if cmp<0:
            parent.left=TreeNode(val)
        else:
            parent.right=TreeNode(val)
        return root
            
        
        
# @lc code=end

