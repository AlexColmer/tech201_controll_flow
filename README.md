# Control flow
flow through a particular decision process 

all about making decisions in the program 

### if statements 
use if, elif and else to write a program

simple film rating program

``` 
film_rating = "universal"

if film_rating.lower() == "universal":
    print("All age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance advised")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12, supervision is recommended")
elif film_rating.lower() == "15":
    print("You must be 15 to watch 15 rated movies in the cinema")
elif film_rating.lower() == "18":
    print("You must be 18 to watch 18 movies in the cinema") 
else:
    print("This is not a correct rating, please use universal, pg, 12 or 12a, 15, 18")
```
there are no 'switch statements' or 'case statements' used in other languages

### For loops

define an iterator number and cycle through data (list or dictionary) 'for each entry in the data structure'
```
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}
             
for num in list_data:
    print(num * 2)
```

nested for loops within dictionaries 

```
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```
how to get a specific items in a dictionary 
```
for items in dict_data.values():
    print(items["money"])
```

if statement in a for loop 
```
list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found three!")
    elif num > 3:
        print("Gone too far!")#
    else:
        print("Too soon")
```

### while loops

something that monitors data rather than iterate. use it to varify user input.
```
x = 0
while x < 10:
    print(f"it's working -> {x}")
    x += 1
```

while loop breaks
```
while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1
```

asking for someone's age
```
user_prompt = True
while user_prompt:
    age = input("What is your age?")
    if age.isdigit():
        user_prompt = False
    else:
        print("please provide your answer in digits")
print(f"your age is {age}")
```