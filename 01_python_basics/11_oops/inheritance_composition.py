class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding Cardamom, Ginger, Cloves")


masala_chai1 = MasalaChai("Masala")
# masala_chai1.add_spices()
# print(masala_chai1.type)


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
print(shop.chai.type)

fancy_chai = FancyChaiShop()
fancy_chai.serve()
