user_seat_type=input("Enter your seat type (sleeper/ AC/ general/ luxury): ").lower()

match user_seat_type:
    case "sleeper":
        print("Sleeper is sleeper class no ac but beds available")
    case "ac":
        print("ac is ac class ac present, beds available")
    case "general":
        print("general is general class, beds not available")
    case "luxury":
        print("luxury is luxury class")
    case _:
        print("No reservation")