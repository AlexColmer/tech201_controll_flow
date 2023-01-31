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
```
there are no 'switch statements' or 'case statements' used in other languages
