#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (54.98%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    12.3K
# Total Submissions: 22.3K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
# 
# 示例 1:
# 
# 输入: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 
# 示例 2:
# 
# 输入: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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
    def rob(help, root: TreeNode) -> int:
        #这里其实是递归的想法，一般的递归s就是考虑一个值，其他交给递归
        '''
        def help(root):
            if root is None:
                return 0
            map={}#利用字典降低时间复杂度
            if root in map:
                return map[root]
            do_it=root.val#如果抢第一个根节点
            if root.left:
                do_it+=help(root.left.left)+help(root.left.right)
            if root.right:
                do_it+=help(root.right.left)+help(root.right.right)
            not_do=help(root.left)+help(root.right)
            res=max(do_it,not_do)
            map[root]=res
            return map[root]
        return help(root)
        '''
        
   

        def helper(root): 
            if not root:
                return 0, 0
            left, prev1 = helper(root.left)
            right, prev2 = helper(root.right)
            return max(prev1 + prev2 + root.val,  left + right), left + right
            #树形动态规划分析时间复杂度
        
        return helper(root)[0]


# @lc code=end

