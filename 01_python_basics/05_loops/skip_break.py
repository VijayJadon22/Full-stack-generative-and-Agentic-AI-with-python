
flavors=["ginger","chocolate","out of stock","lemon","discontinued","tulsi"]

for flavor in flavors:
    if flavor=="out of stock":
        continue
    elif flavor=="discontinued":
        print("Discontinued item found")
        break
    else:
        print(flavor)

print("Outside of loop")

        