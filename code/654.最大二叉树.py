#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode-cn.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (78.13%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 11.9K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
# 
# 
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 
# 
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
# 
# 
# 
# 示例 ：
# 
# 输入：[3,2,1,6,0,5]
# 输出：返回下面这棵树的根节点：
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# 
# 提示：
# 
# 
# 给定的数组的大小在 [1, 1000] 之间。
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        #
        if len(nums)==0:
            return None
        maxvalue=nums[0]
        temp=0
        for i in range(1,len(nums)):#找到最大值，递归左右
            if nums[i]>maxvalue:
                maxvalue=nums[i]
                temp=i
        nums1=nums[:temp]
        nums2=nums[temp+1:]
        root=TreeNode(nums[temp])
        root.left=self.constructMaximumBinaryTree(nums1)
        root.right=self.constructMaximumBinaryTree(nums2)
        return root
        
# @lc code=end

