#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.88%)
# Likes:    347
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 61.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#'[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#
#利用环形链表，然后结合数组来
#双向链表什么是双向链表，因为删除要o(1)必须要可以访问自己的节点
# @lc code=start
#用字典加双向链表来实现
class LRUCache():

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        #新建两个节点
        self.head=Node()
        self.tail=Node()
        #构成环形链表
        self.head.next=self.tail
        self.tail.pre=self.head#注#注意尾部和头部是不加入MAP里面的

    def remove(self,node):
        """定义一个删除的节点的操作，同时删除map
        """
        del self.map[node.key]
        node.pre.next=node.next
        node.next.pre=node.pre 
        
    
    def add_head(self,node):
        """定义将节点移动到头部

        """
        node.next=self.head.next
        self.head.next.pre=node
        node.pre=self.head
        self.head.next=node
        self.map[node.key]=node
    
        

    def get(self, key: int) -> int:
        if key in self.map:#如果在字典里面将节点移动到头部
            res=self.map[key]
            self.remove(res)
            self.add_head(res)
            return res.val

        else:
            return-1
        

    def put(self, key: int, value: int) -> None:
        node=Node(key,value)
        if key in self.map:
            self.map[key].val=value
            res=self.map[key]
            self.remove(res)
            self.add_head(res)
        else:
            if len(self.map)==self.capacity:#如果容量已经满了
                self.remove(self.tail.pre)
                self.add_head(node)
            else:
                self.add_head(node)#将新增加的节点加入map


class Node():#双向链表的节点
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.pre=None
        self.next=None



        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

