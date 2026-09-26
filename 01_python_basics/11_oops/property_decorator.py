class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be greater than 0 and less than 6")


leaf = TeaLeaf(5)
print(leaf.age)
