#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (46.02%)
# Likes:    383
# Dislikes: 0
# Total Accepted:    96.8K
# Total Submissions: 210.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #对于两个
        #这里多开辟了空间nums_copy,可以进行优化
        '''
        nums1_copy=nums1[:m]
        index1=0
        index2=0
        i=0
        while index1<m and index2<n:
            if nums1_copy[index1]<=nums2[index2]:
                nums1[i]=nums1_copy[index1]
                index1+=1
            else:
                nums1[i]=nums2[index2]
                index2+=1
            i+=1
        if index1<m:
            nums1[i:]=nums1_copy[index1:]
        if index2<n:
            nums1[i:]=nums2[index2:]
        return nums1    
        '''
        index1,index2=m-1,n-1
        i=n+m-1
        while index1>=0 and index2>=0:
            if nums1[index1]>=nums2[index2]:
                nums1[i]=nums1[index1]
                index1-=1
            else:
                nums1[i]=nums2[index2]
                index2-=1
            i-=1
        if index1>=0:
            nums1[:i+1]=nums1[:index1+1]
        if index2>=0:
            nums1[:i+1]=nums2[:index2+1]
        







# @lc code=end

