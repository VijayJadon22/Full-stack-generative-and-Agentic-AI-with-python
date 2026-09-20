def brew_chai(flavor):
    try:
        if flavor not in ["masala", "elaichi", "lemon"]:
            raise ValueError(f"{flavor} chai not in stock")

        print(f"{flavor} chai is brewing...")
    except ValueError as e:
        print("Value error:", e)


brew_chai("masala")
brew_chai("ginger")  # Value error: ginger chai not in stock
