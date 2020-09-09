import threading
import time

def producer():
    time.sleep(10)
    print("FOund Prod")
    product.set()
    product.clear()

def consumer():
    print("prodict Wait")
    product.wait()
    print("Product Exists")

product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()