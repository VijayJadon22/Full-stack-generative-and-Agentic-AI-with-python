class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping chai")

    def add_sugar(self, amount):
        self.amount = amount
        print("Sugar added")

    def how_is_chai(self):
        print(f"Chai is good with {self.amount} chai and {self.sweetness} sweetness")


elaichi_tea = Chai(sweetness=3,milk_level=2)
elaichi_tea.add_sugar(amount=4)
elaichi_tea.how_is_chai()
