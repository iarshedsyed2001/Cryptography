#Daemon and Non Daemon threads
#By default all the threads are Non Daemon. It means they complete their assigned target.
#It is possible to turn a thread as Daemon, before activation, by setting its daemon attribute to True.
#Once a thread is turned Daemon then it executes as long as:
#1) Its target is complete.
#2) Other non daemon threads are running.
# whichever first.
#That is a daemon thread terminates prematurely if all other non daemon threads end.
#Know that threads are turned daemon for execution of background tasks, that end prematurely
#as the foreground activities get over.

import threading

class MyThread(threading.Thread):
    def __init__(self, flag):
        #init the super class (threading.Thread) first
        threading.Thread.__init__(self)
        self.flag = flag
        if flag == 3:
            self.daemon = True

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
        for i in range(10000):
            print(val, end = ' ')
        print(' B ends ')

    def fx3(self):
        print(' C starts ')
        for i in range(100000):
            print(' C ', end = ' ')
        print(' C ends ')


def main():
    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)

main()
