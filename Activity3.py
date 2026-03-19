print("Select your ride ")
print("1. bike"    )
print("2. car")



choice = int(input("Enter your choice: "))


if(choice == 1):
    print("You have selected bike")
    print("Select your bike ")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = int(input("Enter your choice2: "))
    if(choice2 == 1):
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif(choice == 2):
    print("You have selected car")
    print("Select your car ")
    print("1. Sedan")
    print("2. XUV")

    choice3 = int(input("Enter your choice3: "))
    if(choice3 == 1):
        print("You have selected Sedan")
    else:
        print("You have selected XUV")

else:
    print("Wrong choice")