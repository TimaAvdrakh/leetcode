import threading
import time
""" 
    Lock When one Thread Locks 
    and as if it locked again
    this couse DEADLOCK
    when it was locked by some
    thread and checked again 
"""
def producer():
    print("set locking")
    with lock:
        print("done")
        with lock:
            print("Its great")
    print("Lokingg release")

lock = threading.Lock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()