class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_data):
        tea_type, sweetness, size = order_data.split("-")
        return cls(tea_type, sweetness, size)


order1 = ChaiOrder.from_dict(
    {"tea_type": "Masala", "sweetness": "strong", "size": "small"}
)
print(order1.tea_type, order1.sweetness, order1.size)

order2 = ChaiOrder.from_string("Lemon-Strong-Big")
print(order2.tea_type, order2.sweetness, order2.size)

order3=ChaiOrder("Ginger","mild","medium")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
