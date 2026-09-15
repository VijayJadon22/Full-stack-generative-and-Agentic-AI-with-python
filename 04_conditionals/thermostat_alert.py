device_status = input("What is the device status currently: ")

if device_status.lower() == "active":
    temperature = input("What is the temperature: ")
    if int(temperature) > 35:
        print("Warning High Temperature!")
    else:
        print("Temperature is normal!")
else:
    print("Device is offline")
