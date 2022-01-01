#Multithreading: Concurrent Execution of subtasks of an application

import threading
def fx1():
    print(' A starts ')
    for i in range(1000):
        print(' A ', end = '')
    print(' A ends ')

def fx2(val):
    print(' B starts ')
    for i in range(1000):
        print(val, end = ' ')
    print(' B ends ')


def main():
    #SEQUENTIAL EXECUTION
    fx1()
    fx2('B')
    #CONCURRENT EXECUTION
    t1 = threading.Thread(target=fx1)
    t2 = threading.Thread(target=fx2, args=('B'))
    t1.start() #thread activation (causes concurrent execution of fx1)
    t2.start() #thread activation (causes concurrent execution of fx2)
main()

