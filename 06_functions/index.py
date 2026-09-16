def get_user():
    return input("Enter user name: ")


def register_user():
    user = get_user()
    print(f"User: {user} registered in DB")

register_user()