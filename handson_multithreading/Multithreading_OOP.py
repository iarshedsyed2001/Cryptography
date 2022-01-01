import threading
#multithreading by inheriting threading.Thread class

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
        elif self.flag == 3:
            self.fx3()

    def fx1(self):
        print(' A starts ')
        for i in range(1000):
            print(' A ', end = '')
        print(' A ends ')

    def fx2(self, val):
        print(' B starts ')
        for i in range(1000):
            print(val, end = ' ')
        print(' B ends ')

    def fx3(self):
        print(' C starts ')
        for i in range(1000):
            print(' C ', end = ' ')
        print(' C ends ')


def main():
    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)

main()
