import ctypes
import time
print(ctypes.windll.user32.BlockInput(True))
print(ctypes.windll.user32.LockWorkStation())
time.sleep(20)

