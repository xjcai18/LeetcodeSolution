import threading
import time
s_driver=threading.Semaphore(1)#初始化为1
s_seller=threading.Semaphore(0)#初始化为0

def driver():
    for i in range(3):
        s_driver.acquire()
        print("开车")
        print("驾驶中")
        print("停车")
        s_seller.release()

def seller():
    for i in range(3):
        s_seller.acquire()
        print("开门")
        print("关门")3
        print("*"*20)
        s_driver.release()

thread_1=threading.Thread(target=driver)
thread_2=threading.Thread(target=seller)
thread_1.start()
thread_2.start()
thread_2.join()
thread_1.join()
print("-"*20)
print("旅行结束")

import threading 
class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1=threading.Semaphore(1)
        self.s2=threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.s1.acquire()#用信号量来控制同步
            printFoo()
            self.s2.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.s2.acquire()
            printBar()
            self.s1.release()