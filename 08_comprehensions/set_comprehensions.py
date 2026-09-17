menu = [
    "lemon tea",
    "iced tea",
    "iced coffee",
    "masala chai",
    "green tea",
    "ginger tea",
    "green tea",
]

unique_chai = {tea for tea in menu}

print(unique_chai)

desired_length = {chai for chai in menu if len(chai) > 10}

print(desired_length)


recipes = {
    "masala chai": ["ginger", "elaichi", "masala"],
    "elaichi chai": ["milk", "elaichi"],
    "lemon chai": ["lemon", "milk"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
