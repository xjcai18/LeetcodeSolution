#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (69.56%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 23K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 
# 示例:
# 
# 给定的有序链表： [-10, -3, 0, 5, 9],
# 
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #先要遍历链表得到列表
        res=[]
        while head != None:
            res.append(head.val)
            head=head.next
        def buildTree(nums,begin,end):
            if begin >end:
                return None
            mid=(begin+end)//2
            root=TreeNode(nums[mid])
            root.left=buildTree(nums,begin,mid-1)#列表z中间左边的都在左子树
            root.right=buildTree(nums,mid+1,end)#列表右边的都在右子树
            return root
        if len(res)==0:
            return None
        
        return buildTree(res,0,len(res)-1)
    

        
# @lc code=end