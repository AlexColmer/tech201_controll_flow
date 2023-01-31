user_prompt = True

age = input("What is your age? ")
if age.isdigit() and int(age) < 117 and int(age) > 1:
    user_prompt = False
else:
    print("the value you have entered is invalid pleas enter a digit between 0 - 117 for example 12")

if age.isdigit() and 0 < int(age) < 117:
    if int(age) >= 18:
        print("You can watch all films")
    elif int(age) < 18 and int(age) >= 15:
        print("You can watch u, pg, 12, 12a and 15")
    elif int(age) < 15 and int(age) >= 12:
        print("You can watch u, pg 12 and 12a")
    elif int(age) < 12:
        print("You can only watch u and pg films")


