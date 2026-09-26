class OutOfIngredientsError(Exception):
    pass


def make_tea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Ingredients out of stock")
    print("Making tea..")

make_tea(0,2)