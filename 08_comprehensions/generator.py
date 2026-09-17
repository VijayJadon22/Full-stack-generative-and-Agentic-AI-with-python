daily_sales = [1, 5, 3, 6, 10, 12, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
