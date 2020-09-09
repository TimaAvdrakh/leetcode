import threading
import time

def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)

results = []
params = {
    "finished" : 2**20
}

task1 = threading.Thread(
    target=handler,
    kwargs={
        "finished" : 2**10
    })

task2 = threading.Thread(
    target=handler,
    kwargs= {
        "started": 2**10,
        "finished": 2**20
    }
)

start_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()
print("Results 1")
print("TIme {}".format(time.time() - start_at))
print("value", sum(results))

results = []
start_at = time.time()
handler(finished=2**20)
print("Results 1")
print("TIme {}".format(time.time() - start_at))
print("value", sum(results))
