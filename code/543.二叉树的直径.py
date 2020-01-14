#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (46.45%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 34.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
# 
# 示例 :
# 给定二叉树
# 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
# 
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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
    '''
    采用分治和递归的思想：
    - 根节点为root的二叉树的直径 = 
    max(root->left的直径，root->right的直径，root->left的最大深度+root->right的最大深度+1)
    '''
    def __init__(self):
        self.sum=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.sum
        
    def depth(self,root):
        if root is None:
            return 0
        l=self.depth(root.left)
        r=self.depth(root.right)
        self.sum=max(self.sum,l+r)
        return max(l,r)+1#这个是求最大深度的返回值

        
        
# @lc code=end

