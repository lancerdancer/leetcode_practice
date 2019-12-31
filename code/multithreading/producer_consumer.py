import threading
import queue

BUF_SIZE = 3


class Threading:

    q = queue.Queue(BUF_SIZE)
    lock = threading.Lock()
    c_cons = threading.Condition(lock)  # consumer waits on this cond var
    c_prod = threading.Condition(lock)  # producer waits on this cond var

    def producer(self):
        for i in range(1, 21):
            self.c_prod.acquire()

            while self.q.full():  # block if buffer is full
                self.c_prod.wait()

            self.q.put(i)

            self.c_prod.release()

            self.c_cons.acquire()
            self.c_cons.notify()
            self.c_cons.release()
            print("producer: inserted {}\n".format(i))

        print("producer quiting\n")
        exit(0)

    def consumer(self):
        while True:
            self.c_cons.acquire()

            while self.q.empty():
                self.c_cons.wait()

            i = self.q.get()

            self.c_cons.release()

            self.c_prod.acquire()
            self.c_prod.notify()
            self.c_prod.release()
            print("Consume value {}\n".format(i))


if __name__ == "__main__":
    thread = Threading()

    tp = threading.Thread(target=thread.producer)
    tc = threading.Thread(target=thread.consumer)

    tp.start()
    tc.start()

    tp.join()
    tc.join()
