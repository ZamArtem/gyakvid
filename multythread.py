# GIL = (global interpreter lock),



import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("U ate breakfast")

def dring_coffee():
    time.sleep(4)
    print("U drink coffee")
def study():
    time.sleep(5)
    print("U finished studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=dring_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


x.join()
y.join()
z.join()

#eat_breakfast()
#dring_coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
