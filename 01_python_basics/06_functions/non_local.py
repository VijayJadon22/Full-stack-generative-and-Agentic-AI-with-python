# def update_item_order():
#     item_category = "Tshirts"

#     def inner_func():
#         item_category = "Shirts"
#         print(f"Inner Item category is {item_category}")

#     inner_func()
#     print(f"Outer Item category is {item_category}")


# update_item_order()


def update_item_order():
    item_category = "Tshirts"

    def inner_func():
        nonlocal item_category
        item_category = "Shirts"
        print(f"Inner Item category is {item_category}")

    inner_func()
    print(f"Outer Item category is {item_category}")


update_item_order()
