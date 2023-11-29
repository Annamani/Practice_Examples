import threading
import time
def longSquare(num):
    time.sleep(1)
    return num**2

[longSquare(n) for n in range(0, 5)]
t1 = threading.Thread(target=longSquare, args=(1,))
t2 = threading.Thread(target=longSquare, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()