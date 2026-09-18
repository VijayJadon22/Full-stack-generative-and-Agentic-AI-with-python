def local_chai():
    yield "Masala chai"
    yield "Lemon chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


