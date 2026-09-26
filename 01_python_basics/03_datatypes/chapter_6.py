essential_items = {"Pant", "shirt", "socks", "socks"}

optional_items = {
    "handkerchief",
    "gloves",
    "socks",
}  # socks appear twice in both essential and optional

all_items = essential_items | optional_items

print(
    all_items
)  # =>{'Pant', 'socks', 'handkerchief', 'gloves', 'shirt'} socks present only once as this is intersection

common_items = essential_items & optional_items

print(common_items)
print(essential_items)
