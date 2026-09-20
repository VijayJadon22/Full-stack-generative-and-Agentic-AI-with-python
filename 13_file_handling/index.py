file = open("order.txt", "w")

try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()
