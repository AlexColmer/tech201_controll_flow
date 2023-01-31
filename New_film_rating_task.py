age = input("What is your age? ")

if age.isdigit() and int(age) > 0 and int (age) < 117:
    if int(age) >= 18:
        print("You can watch all films")
    elif int(age) < 18 and int(age) >= 15:
        print("You can watch u, pg, 12, 12a and 15")
    elif int(age) < 15 and int(age) >= 12:
        print("You can watch u, pg 12 adn 12a")
    else:
        print("You can only watch u and pg films")
else:
    ("the value you have enterd is invlaid pleas enter a digit for example 12")