#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (36.73%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    29.5K
# Total Submissions: 79.4K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 示例 1:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # write code here
        #这个是复杂度肯定不是最好
        index=-1
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        left=0
        right=len(matrix)-1
        while left <=right:
            
            middle=(left+right)//2
            if matrix[middle][0]>target:
                right=middle-1
            elif matrix[middle][-1]<target:
                left=middle+1
            else:
                index=middle
                break

        if index==-1:
            return False
        low=0
        high=len(matrix[0])-1
        while low<=high:
            middle=(low+high)//2
            if matrix[index][middle]==target:
                return True
            elif matrix[index][middle]<target:
                low=middle+1
            else:
                high=middle-1
        return False
        
# @lc code=end

