import threading
import time
def longSquare(num):
    time.sleep(1)
    return num**2

[longSquare(n) for n in range(0, 5)]