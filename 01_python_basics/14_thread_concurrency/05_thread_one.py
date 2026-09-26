import threading
import time


def boil_milk():
    print("Milk is boiling...")
    time.sleep(2)
    print("Milk is boiled")


def toast_bun():
    print("Bun is toasting..")
    time.sleep(3)
    print("Bun is toasted")


start = time.time()
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds")
