altd=int(input("Please enter the plane altitude \n"))
if (altd<1000):
    print("You can land the plane ")
elif (altd<5000):
    print("Come down to 1000 ft")

else:
    print("Go around and try later")