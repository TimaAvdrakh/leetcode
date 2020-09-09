import threading
import time

def producer():
    print("Set locking")
    with lock:
        with lock:
            print("its great")
    print("Looking release")


""" 
    RLock for recursive processes with threads
"""
lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()