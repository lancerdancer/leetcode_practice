"""
Priority Readers and Writers
Write a multi-threaded C program that gives readers priority over writers concerning a shared (global) variable.
Essentially, if any readers are waiting, then they have priority over writer threads -- writers can only write when
there are no readers. This program should adhere to the following constraints:

Multiple readers/writers must be supported (5 of each is fine)
Readers must read the shared variable X number of times
Writers must write the shared variable X number of times
Readers must print:
    The value read
    The number of readers present when value is read
Writers must print:
    The written value
    The number of readers present were when value is written (should be 0)
Before a reader/writer attempts to access the shared variable it should wait some random amount of time
    Note: This will help ensure that reads and writes do not occur all at once
Use pthreads, mutexes, and condition variables to synchronize access to the shared variable

"""
import threading
from random import randint
from time import sleep

X = 20
VAR = -1
READER_NUM = 0
WRITING = False
W_CON = threading.Condition()
R_CON = threading.Condition()


def reader():
    global READER_NUM

    for _ in range(X):
        sleep(randint(1, 100) / 1000)

        # Enter critical section
        R_CON.acquire()
        while WRITING:
            R_CON.wait()
        READER_NUM += 1
        R_CON.release()

        # Read data
        print('reader: {}, reader present: {}'.format(VAR, READER_NUM))

        # Exit critical section
        READER_NUM -= 1
        W_CON.acquire()
        if READER_NUM == 0:
            W_CON.notify()
        W_CON.release()


def writer():
    global VAR
    global WRITING

    for num in range(X):
        sleep(randint(1, 100) / 1000)

        # Enter critical section
        W_CON.acquire()
        while READER_NUM != 0 or WRITING:
            W_CON.wait()
        WRITING = True
        W_CON.release()

        # Write data
        VAR = num
        print('writer: {}, reader present: {}'.format(VAR, READER_NUM))

        # Exit critical section
        R_CON.acquire()
        WRITING = False
        R_CON.notify_all()
        R_CON.release()


if __name__ == "__main__":
    tws = []
    trs = []

    for i in range(5):
        tw = threading.Thread(target=writer)
        tr = threading.Thread(target=reader)
        tws.append(tw)
        trs.append(tr)

    for i in range(len(tws)):
        tws[i].start()
        trs[i].start()

    for i in range(len(tws)):
        tws[i].join()
        trs[i].join()

