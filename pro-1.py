age = int(input("Enter your age: "))
if age >= 18:
    id_proof = input("Do you have a valid ID proof? (y/n): ")
    
    if id_proof == "y":
        print("You can vote.........!")
    else:
        print("You need an ID to vote.........!")
        
else:
    print("You cannot vote..........!")