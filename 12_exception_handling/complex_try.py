def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai")
        if flavor == "unknown":
            raise ValueError("Please specify flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is prepared")
    finally:
        print(f"{flavor} chai is coming to your table")


user_input = input("Which flavor chai would you like? :")
serve_chai(flavor=user_input)
