#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (71.94%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 43.5K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    #没有剪枝的dfs
    def combine(self, n: int, k: int) :
        result=[]
        path=[]
        
        self.backtacking(n,k,1,path,result)
        
        return result
        
    def backtacking(self,n,k,start,path,result):
        if k<0:
            return #
        elif k==0:#满足条件，跳出递归
            result.append(path[:])#这里也是因为引用类型
            print("最后答案",path)#[1,2,3]
            print("*"*40)
             #思考这里为什么去掉还是可以运行
        else:
            for i in range(start,n+1):#n=5,k=3【1,2,3】
                #取到[1,2,3]后3弹出变成[1,2]#backtracking(n,0,)
                print("进入循环")
                print("i的值是:",i)
                path.append(i)
                print("进入递归前k的值是:",k)
                print("进入下一层递归")
                self.backtacking(n,k-1,i+1,path,result)#k相当于层数，退回的时候会倒退？
                print("退出下一层递归k的值是:",k)
                print("推出下一层后i的值是：", i)
                print("返回上一层递归")
                print("回溯前的值",path)
                path.pop()#[1,2] 从这里结束后程序到到哪里了
                print("回溯后的值:",path)
                

s=Solution()
s.combine(5,3)
            
        
# @lc code=end

