#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (61.43%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    34K
# Total Submissions: 55.2K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 
# 
# 示例 2:
# 
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #利用二叉搜索树
        #定义一个节点是否在其中的函数z，这里是搜索二叉树，可以比较大小
        #什么时候推出循环
        '''
        def help(root,node):
            """判断node是否在root里面：

            """
            if not root:
                return False
            queue=[root]
            while queue:
                root=queue.pop(0)
                if root==node:
                    return True
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            return False

        
        #写一个循环什么时候推出循环呢
        node=root
        i=1
        while i==1:
            if node.left and help(node.left,p) and help(node.left,q):
                node=node.left
                i+=1
            if node.right and help(node.right,p) and help(node.right,q):
                node=node.right
                i+=1
            i-=1

        return node
        '''
        '''
        parent=root.val
        p_val=p.val
        q_val=q.val
        if p_val >parent and q_val>parent:
            return self.lowestCommonAncestor(root.right,p,q)
        if p_val<parent and q_val <parent:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        '''
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

            
        
# @lc code=end

