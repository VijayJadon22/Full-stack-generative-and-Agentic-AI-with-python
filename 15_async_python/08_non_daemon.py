import threading
import time


def monitor_tea_temp():
    while True:
        print("Monitoring Tea Temp...")
        time.sleep(2)


t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main Program Done")
