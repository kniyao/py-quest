age = input("What is your age")

while int(age) < 15 or int(age) > 100:
    print ("sorry you cannot ride the roller coster")
    nextAge = input("What is your age:")
    if int(nextAge) > 15 and int(nextAge) < 65:
            print("Good luck on your ride, you can now eneter the roller coster")
            break
    