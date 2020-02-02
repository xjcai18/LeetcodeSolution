#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (51.83%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    73.1K
# Total Submissions: 140.1K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #如果把其放在一个数组里面，怎么区分呢，可以分值
        #构造一个字典
        phone={}
        phone['2']=["a","b","c"]
        phone['3']=["d","e","f"]
        phone['4']=["g","h","i"]
        phone['5']=["j","k","l"]
        phone['6']=["m","n","o"]
        phone['7']=["p","q","r","s"]
        phone['8']=['t','u','v']
        phone['9']=["w","x","y","z"]
        #分而治之的想法，前提是将递归的条件先确定好不可以进入了无限递归的状态
        '''
        if len(digits)==0:
            return 
        if len(digits)==1:
            return phone[digits[0]]
        first=phone[digits[0]]
        digits=digits[1:]
        result=[]
        for word in (first):
            for res in self.letterCombinations(digits):
                ans=word+res
                result.append(ans)
        return result
        '''
        if len(digits)==0:
            return []
        result=[]
        self.backtrack(0,digits,phone,"",result)
        return result
    def backtrack(self,depth,digits,phone,path,result):
        if len(digits)==depth:
            result.append(path)
        else:
            for value in phone[digits[depth]]:
                path+=value
                self.backtrack(depth+1,digits,phone,path,result)
                path=path[:-1]
        




        
# @lc code=end

