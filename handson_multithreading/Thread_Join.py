#Thread Joins
#A thread join suspends the current thread (one that calls joins) until a target thread completes.
#Example :
#There are two threads ThreadA and ThreadB.
#At line number n, ThreadA executes a call like :
#   ThreadB.join()
#This would suspend ThreadA until ThreadB completes.
#If ThreadB was already complete then join would not cause any suspension.


import threading

class MyThread(threading.Thread):
    def __init__(self, flag):
        #init the super class (threading.Thread) first
        threading.Thread.__init__(self)
        self.flag = flag
        self.start() #thread activation (has target: self.run)

    #override run as it is the target of thread
    def run(self):
        if self.flag == 1:
            self.fx1()
        elif self.flag == 2:
            self.fx2(' B ')

    def fx1(self):
        print(' A starts ')
        for i in range(1000):
            print(' A ', end = '')
        print(' A ends ')

    def fx2(self, val):
        print(' B starts ')
        for i in range(10000):
            print(val, end = ' ')
        print(' B ends ')


def main():
    #let A and B be printed concurrently
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.join() #suspend the current thread ( main thread) until t1 is active
    print('****')
    t2.join()#suspend the current thread ( main thread) until t2 is active
    #let C be printed after A/B  print is complete
    print(' Main starts ')
    for i in range(100000):
        print(' C ', end=' ')
    print(' Main ends ')


main()
