import threading
import time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)


def brewing_chai():
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        time.sleep(3)


# Create thread
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brewing_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print("All orders are placed and chai brewed")
