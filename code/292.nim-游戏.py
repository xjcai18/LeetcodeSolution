#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#
# https://leetcode-cn.com/problems/nim-game/description/
#
# algorithms
# Easy (69.62%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    35.6K
# Total Submissions: 51.1K
# Testcase Example:  '4'
#
# 你和你的朋友，两个人一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
# 
# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
# 
# 示例:
# 
# 输入: 4
# 输出: false 
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
# 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
# 
# 
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        '''
        #4 F 自己一定会输，如果让对手拿到4一定可赢
         5 T
         6 T
         7 T#如果自己拿到
         8 F
         9 T
         10T
        11 T
        12 F
        '''
        return n%4 !=0

# @lc code=end

