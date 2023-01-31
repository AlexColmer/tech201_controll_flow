x = 0

# while x < 10:
#     print(f"it's working -> {x}")
#     x += 1

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break
#     x += 1
#
# print(x)

# asking for someone's age
# this can be either an int (20) or a string (twenty)

# age = input("What is your age?")
#
# print(f"your age is {age}")
user_prompt = True
while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("please provide your answer in digits and below 117")
print(f"your age is {age}")
