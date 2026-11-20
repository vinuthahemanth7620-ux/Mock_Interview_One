age = int(input("Enter your age: "))
weekend = input("Is it a weekend? (y/n): ")

if age <= 18:
    if weekend == "y":
        print("Ticket Price: ₹150")
    else:
        print("Ticket Price: ₹100")

elif age <= 60:
    if weekend == "y":
        print("Ticket Price: ₹350")
    else:
        print("Ticket Price: ₹300")

elif age <= 80:
    if weekend == "y":
        print("Ticket Price: ₹250")
    else:
        print("Ticket Price: ₹200")

else:
    print("Please take care of yourself.....!")