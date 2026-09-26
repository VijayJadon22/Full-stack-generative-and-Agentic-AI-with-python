list_items=["Pant","shirt","socks"]
list_items2=["Cargo"]

print(list_items)

list_items.append("joggers")
print(list_items)
print(len(list_items))
list_items.extend(list_items2)
print(list_items)
list_items.sort()
print(list_items)

sugar_levels=[1,2,3,4,5,6,7,8,9]
print(max(sugar_levels))

#Operator overloading

liquids=["water","sugar_syrup"]
liquid2=["ginger"]

liquid_mix=liquids+liquid2
print(liquid_mix)