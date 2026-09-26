price_list = {"small": 10, "medium": 15, "large": 20}

user_input = input("Enter the tea cup size you want to drink: ")

if user_input.lower() == price_list["small"]:
    print(f"Your tea price is {price_list['small']}")
elif user_input.lower() == price_list["medium"]:
    print(f"Your tea price is {price_list['medium']}")
else:
    print(f"Your tea price is {price_list['large']}")
