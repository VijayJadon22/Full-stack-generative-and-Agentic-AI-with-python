# import categories.items

# print(categories.items.return_tshirts())
# print(categories.items.return_pants())


from categories.items import return_tshirts as tshirts, return_pants as pants

print(tshirts())
print(pants())
