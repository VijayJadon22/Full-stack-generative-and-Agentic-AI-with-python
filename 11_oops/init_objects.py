class Chaiorder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"This is {self.type} chai of {self.size} cup"


order = Chaiorder(type_="Masala", size=2)
print(order.summary())

order2 = Chaiorder("Lemon", 5)
print(order2.summary())

