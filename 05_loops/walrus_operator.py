# value = 13

# if remainder := value % 5:
#     print(f"Not divisible, remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter the desired size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

flavors=["ginger","masala","lemon","mint"]

print("Available flavors ",flavors)

while (flavor := input("Choose the flavor: ")) not in flavors:
    print(f"Sorry {flavor} is not available")
print(f"You choose {flavor} chai")

