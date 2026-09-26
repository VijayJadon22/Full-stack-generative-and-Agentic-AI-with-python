class Chaicup:
    size = 150  # ml

    def describe(self):
        return f"A {self.size}ml chai cup"


cup = Chaicup()
cup2 = Chaicup()
cup2.size = 100
print(cup.describe())
print(cup2.describe())

# print(Chaicup.describe()) #error

print(Chaicup.describe(cup2))
