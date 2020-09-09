import threading
import time

""" 
    Семофор для ограничений количество воркеров или потоков 
    (если поставить 1 то будет рабоать как синхронная прога
"""

def producer():
    with lock:
        print("set locking", lock._value)
        time.sleep(3)
        print("im free")


max_workers = 3
lock = threading.Semaphore(value=max_workers)

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
task3 = threading.Thread(target=producer)
task4 = threading.Thread(target=producer)
task5 = threading.Thread(target=producer)

task1.start()
task2.start()
task3.start()
task4.start()
task5.start()


task1.join()
task2.join()
task3.join()
task4.join()
task5.join()
lock.release()
