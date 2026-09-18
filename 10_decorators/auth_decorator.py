from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied, admins only!")

        else:
            return func(user_role)

    return wrapper


@require_admin
def access_item_inventory(role):
    print("Access granted to item inventory")

access_item_inventory("admin")
