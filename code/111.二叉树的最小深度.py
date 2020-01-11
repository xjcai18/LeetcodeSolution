#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (40.82%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    43.7K
# Total Submissions: 107K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        '''
        #迭代BFS遍历
        if not root:
            return 0
        queue=[(1,root)]
        while queue:
            depth,node=queue.pop(0)#队列这里是BFS #
            children=[node.left,node.right]

            if not any(children):
                return depth #为什么这里没有比较，或者说为什么不必须比较，因为BFS是一层一层得遍历
            for child in children:
                if child:
                    queue.append((depth+1,child))
        return depth
        '''
        if not root:
            return 0
        stack=[(1,root)]
        min_depth=float('inf')
        while stack:
            depth,node=stack.pop()#堆栈
            children=[node.left,node.right]
            
            if not any(children):
                min_depth=min(min_depth,depth)#因为这个是DFS，不是一层一层遍历，这里得depth顺序是乱的
            for child in children:
                if child:
                    stack.append((depth+1,child))
        return min_depth
            
        
        
        
# @lc code=end

