#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (54.72%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 15.2K
# Testcase Example:  '[1,null,3,2]'
#
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
# 
# 示例 :
# 
# 
# 输入:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# 输出:
# 1
# 
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
# 
# 注意: 树中至少有2个节点。
#         1
#        / \
#       2   3
#      /   / \
#     4   2   1
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        '''
        def help(root):#这里求得是任意相邻差最小得
            if root is None:
                return 0
            if root.left:
                res.append(abs(root.val-root.left.val))
            if root.right:
                res.append(abs(root.val-root.right.val))
            help(root.left)
            help(root.right)
            return res
        res=[]
        res=help(root)
        print(res)
        return min(res)
        '''

        #先中序遍历
        def inorder(root):#中序遍历以后就是o排序好e的数组
            if root is None:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        res=[]
        res=inorder(root)
        #对于排序好的数组怎么求差值
        #[1,3,6,7,9]
        #[ ,1,3,6,7,9]
        min_value=float('inf')
        for i in range(len(res)-1):
            temp=res[i+1]-res[i]
            if temp<min_value:
                min_value=temp
        return min_value

        
# @lc code=end

