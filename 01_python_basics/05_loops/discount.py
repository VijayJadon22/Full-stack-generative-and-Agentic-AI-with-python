users = [
    {"id": 1, "name": "Aman", "total": 100, "coupon": "p10"},
    {"id": 2, "name": "man", "total": 150, "coupon": "f10"},
    {"id": 3, "name": "an", "total": 120, "coupon": "a10"},
]

discount = {"p10": (0.2, 0), "f10": (0.5, 0), "a10": (0, 10)}

for user in users:
    percentage, fixed = discount.get(user["coupon"])
    discount_amount = user["total"] * percentage + fixed
    final_total = user["total"] - discount_amount
    print(f"User: {user['id']} total payable amount is {final_total}")


item_list = ["socks", "tshirt", "pant"]

if (user_selected_item := input("Enter your item: ").lower()) in item_list:
    print(f"Item is available {user_selected_item}")
else:
    print("Item is not available ")
