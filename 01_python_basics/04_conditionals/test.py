items = ["sOcks", "Pant", "Shirt"]
user_input = input("Enter your preferred Item: ")

items_lower = []

for item in items:
    items_lower.append(item.lower())

print(f"Lowered items: {items_lower}")


if user_input.lower() in items_lower:
    print(f"{user_input} is available in items")
else:
    print(f"{user_input} is not available in items")
