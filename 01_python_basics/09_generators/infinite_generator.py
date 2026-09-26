def infinite_chai():
    count = 1
    while True:
        yield f"Count is {count}"
        count += 1


refill = infinite_chai()

user2 = infinite_chai()

for _ in range(3):
    print(next(refill))

for _ in range(5):
    print(next(user2))
