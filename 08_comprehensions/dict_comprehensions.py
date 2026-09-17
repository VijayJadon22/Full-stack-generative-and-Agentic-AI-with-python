tea_prices_inr = {"masala": 10, "lemon": 20, "spicy": 25, "chocolate": 30}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
