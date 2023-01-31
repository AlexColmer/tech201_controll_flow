# age = 15
#
# if age >= 18:
#     print("Your are the correct age to watch this film and can buy a ticket")
# elif age < 18:
#     print("I'm afraid you cannot watch this movie, you are not old enough")

film_rating = "12"

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