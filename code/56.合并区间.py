#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (39.59%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    49.9K
# Total Submissions: 124.5K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#

# @lc code=start
class Solution:
       def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals = sorted(intervals)
            print(intervals)
            res = []
            n = len(intervals)
            i = 0
            while i < n:#遍历所有的元素}
                left=intervals[i][0]
                right=intervals[i][1]
                while i<n-1 and intervals[i+1][0]<=right:
                    right=max(right,intervals[i+1][1])
                    i+=1
                res.append([left,right])
                i+=1
            return res
# @lc code=end

