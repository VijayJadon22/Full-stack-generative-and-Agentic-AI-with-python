def get_total(bill): #this is pure fucntion as it is not altering any gloabl variable
    return bill + 10


total_Amount = get_total(20)
print(total_Amount)

initial_bill = 0


def calculate_total(amount): #this is impure fucntion as it is altering gloabl variable
    global initial_bill
    initial_bill = 40
    return amount + initial_bill


new_bill = calculate_total(100)
print(f"New bill is: {new_bill}")

print(f"Inital bill: {initial_bill}")
