class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding Cardamom, Ginger, Cloves")


masala_chai1 = MasalaChai("Masala")
masala_chai1.add_spices()
print(masala_chai1.type)
