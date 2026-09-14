item_count = 3
print(f"this is the {item_count} item count")

item_count = 8
print(f"this is the {item_count} item count")

print(f"Id of 3: {id(3)}")
print(f"Id of 8: {id(8)}")

chai_description = "This is a chai description"
print(
    f"{chai_description.split(' ')[0]} {chai_description.split(' ')[1]} {chai_description.split(' ')[3]}"
)
print(chai_description.index("ai"))
print(f"{chai_description[0:7]} {chai_description[10:14]}")
