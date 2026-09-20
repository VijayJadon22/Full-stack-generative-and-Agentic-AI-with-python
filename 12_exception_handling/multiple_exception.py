def process_order(type, quantity):
    try:
        price = {"masala": 20}[type]

        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number")
        cost = price * quantity
        print(f"The total cost of chai is {cost}rs")
    except KeyError:
        print("This chai is not available")
    except TypeError as e:
        print("Type Error:", e)


# process_order("ginger",4) #Will give KeyError: This chai is not available
process_order("masala", "two")
