class InavlidChaiError(Exception):
    pass


def bill(flavor, cups):
    menu = {"masala": 40, "lemon": 30, "elaichi": 25}
    try:
        if flavor not in menu:
            raise InavlidChaiError("Flavor not in menu")
        if not isinstance(cups, int):
            raise TypeError("Please enter cups in number")

        total = menu[flavor] * cups
        print(f"Total cost for {cups} cups of {flavor} chai is {total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting our cafe")


flavor = input("Enter the chai flavor you want: ")
try:
    cups = int(input("Enter the number of cups you want: "))
    bill(flavor=flavor.lower(), cups=cups)

except ValueError:
    print("Please enter the number of cups as a number.")
