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


# Recursive Function

def recursive_function(n):
    if(n==0):
        return "N value is 0"
    print(f"Value of n is: {n}")
    return recursive_function(n-1)

recursive_function(5)
