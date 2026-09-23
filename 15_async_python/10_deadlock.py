import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("task 1 accquired lock_a")
        time.sleep(1)
        with lock_b:
            print("task 1 accquired lock_b")


def task2():
    with lock_b:
        print("task 2 accquired lock_b")
        time.sleep(1)
        with lock_a:
            print("task 2 accquired lock_a")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
