class Chai:
    temperature = "Hot"
    strength = "strong"


masala = Chai()

print(masala.temperature)
print(masala.strength)

masala.strength = "mild"
print(masala.temperature)
print(masala.strength)

del masala.strength
print(masala.strength)

masala.cup=2
print(masala.cup)

del(masala.cup)
print(masala.cup)

