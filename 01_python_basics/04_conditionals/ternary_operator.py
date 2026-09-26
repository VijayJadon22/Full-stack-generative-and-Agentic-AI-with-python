order_amount = int(input("Enter the amount you want to pay: "))

delivery_fees = 0 if order_amount > 300 else 30

print(delivery_fees)