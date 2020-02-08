#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.47%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    54.4K
# Total Submissions: 146.8K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target):

    #回溯法来做这道题
        size=len(nums)
        res=[]
        nums.sort()
        self.backtrack(nums,0,size,target,[],res)
        return res

    def backtrack(self,nums,start,size,target,path,res):
        if len(path)==4 and target==0 and path not in res :
            res.append(path[:])
        elif len(path)==4:
            return
        else:
            for i in range(start,size):
                path.append(nums[i])
                self.backtrack(nums,i+1,size,target-nums[i],path,res)
                path.pop()


if __name__ == "__main__":
    
    s=Solution()
    nums=[-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492]
    target=1682
    a=s.fourSum(nums,target)
    print(a)

        
# @lc code=end

