# Write a code that takes an email as input from the user
# The code will validate the email
# If the input is a valid email, A message should be printed and the code should exit
# If an invalid email is given, there must be an error message and the user must be prompted for another entry
# The user shouldn't be able to give input to the code more than 5 times
# After five consecutive failed inputs, the user must be given a message saying they've been ran out of attempts

         

count = 0
def isItValid():
    global count
    while count < 5:
        email = input("email: ")
        splitEmail = email.split("@")
        if  len(splitEmail) == 2:
            if len(splitEmail[1].split(".")) == 2:
                print("Your email is valid!")
                break
        elif count < 4:
            print("your email is invalid")
            count += 1
        else:
            print("oops!,you can't try again")
            break
            

isItValid()