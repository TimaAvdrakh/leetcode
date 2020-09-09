"""
    In simple words, a thread is a sequence of such instructions within a program that can be executed independently
    of other code. For simplicity, you can assume that a thread is simply a subset of a process!
"""
import threading
import time

def handler(start=0, finish =0):
    result = 0

    for i in range(start,finish):
        result += i
    print(result)

params = {"finish": 2 ** 20}

task = threading.Thread(target=handler, kwargs = params)
started_at = time.time()
print("Results 1")
task.start()
task.join()
print("TIme {}".format(time.time() - started_at))

started_at = time.time()
print('RESULTS 2')
handler(**params)
print("Time {}".format(time.time() - started_at))
