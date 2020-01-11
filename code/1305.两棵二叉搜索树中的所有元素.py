#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
#
# https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (74.10%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 3.1K
# Testcase Example:  '[2,1,4]\r\n[1,0,3]\r'
#
# 给你 root1 和 root2 这两棵二叉搜索树。
# 
# 请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
# 
# 
# 示例 2：
# 
# 输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
# 输出：[-10,0,0,1,2,5,7,10]
# 
# 
# 示例 3：
# 
# 输入：root1 = [], root2 = [5,1,7,0,2]
# 输出：[0,1,2,5,7]
# 
# 
# 示例 4：
# 
# 输入：root1 = [0,-10,10], root2 = []
# 输出：[-10,0,10]
# 
# 
# 示例 5：
# 
# 
# 
# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
# 
# 
# 
# 
# 提示：
# 
# 
# 每棵树最多有 5000 个节点。
# 每个节点的值在 [-10^5, 10^5] 之间。
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root):
            def help(root):
                if not root:
                    return []
                help(root.left)
                res.append(root.val)
                help(root.right)
                return res
            res=[]#在函数外面开始定义一个变量的技巧
            return help(root)
        def merge(nums1,nums2):
            res=[]
            m=len(nums1)
            n=len(nums2)
            p,q=0,0
            while p<m and q<n:
                if nums1[p]<nums2[q]:
                    res.append(nums1[p])
                    p+=1
                else:
                    res.append(nums2[q])
                    q+=1
            if p<m:
                res.extend(nums1[p:])
            if q<n:
                res.extend(nums2[q:])
            return res
        return merge(inorder(root1),inorder(root2))
        
# @lc code=end

