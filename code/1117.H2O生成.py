import threading
class H2O:
    def __init__(self):
        self.s1=threading.Semaphore(2)#H信号量
        self.s2=threading.Semaphore(1)#O信号量
        self.s3=threading.Semaphore(0)#反应条件信号量
        self.s4=threading.Semaphore(0)#反应条件信号量


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.s1.acquire()#保证只有两个H线程进入
        self.s3.release()#释放H原子到达信号
        self.s4.acquire()#等到O原子到达
        releaseHydrogen()
        self.s1.release()#唤醒H线程


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.s2.acquire()#保证一个O线程进入
        self.s4.release()#释放氧原子到达信号，因为有两个H线程等待
        self.s4.release()
        self.s3.acquire()#等待两个H线程到达
        self.s3.acquire()
        releaseOxygen()
        self.s2.release()#唤醒O线程