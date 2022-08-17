while True:
    new_number=input("Enter your number")
    if new_number.isdigit()==True and len(new_number)==10:
        print ("The number is valid")
    else:
        print ("The number is not valid, try again")