import random
while True:
    your_num=int(input("Guess the number please..."))
    real_number=random.randint(1,10)
    if your_num==real_number:
        print("You are right!")
        break
    else:
        print("No, try again")
