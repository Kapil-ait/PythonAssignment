"""============================================================
ASSIGNMENT 7 – MOVIE COLLECTION SYSTEM
======================================

Create a Movie class inside:

models/movie.py

ATTRIBUTES:

* movie_id
* movie_name
* genre
* rating
* ticket_price

TASKS:

1. Take details of 5 movies from the user.
2. Create Movie objects.
3. Store all objects in a list.
4. Display all movies.
5. Display movies having rating greater than 8.
6. Display all Action movies.
7. Find the highest-rated movie.
8. Search a movie using Movie Id.
9. Calculate average movie rating.
10. Display movies whose ticket price is greater than 300.

SAMPLE DATA:

101 Dangal Drama 8.4 250
102 Jawan Action 7.5 300
103 3Idiots Drama 8.4 200
104 Bahubali Action 8.1 350
105 Pathaan Action 7.0 320

EXPECTED OUTPUT:

Movies with rating greater than 8:

Dangal 8.4
3Idiots 8.4
Bahubali 8.1

Action Movies:

Jawan
Bahubali
Pathaan

Highest Rated Movie:

Dangal 8.4

Movies with ticket price greater than 300:

Bahubali 350
Pathaan 320

Average Movie Rating:

7.88

Search Movie Id: 104

Movie Found:

104 Bahubali Action 8.1 350"""
class Movie:

    def __init__(self, movie_id, movie_name, genre, rating, ticket_price):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.genre = genre
        self.rating = rating
        self.ticket_price = ticket_price


movies = []

# Take details of 5 movies
for i in range(5):
    print("\nEnter Movie", i + 1)

    movie_id = int(input("Movie ID: "))
    movie_name = input("Movie Name: ")
    genre = input("Genre: ")
    rating = float(input("Rating: "))
    ticket_price = float(input("Ticket Price: "))

    movies.append(Movie(movie_id, movie_name, genre, rating, ticket_price))


# Display all movies
print("\n--- All Movies ---")

for m in movies:
    print(m.movie_id, m.movie_name, m.genre, m.rating, m.ticket_price)


# Rating greater than 8
print("\n--- Movies with Rating Greater Than 8 ---")

for m in movies:
    if m.rating > 8:
        print(m.movie_name, m.rating)


# Action movies
print("\n--- Action Movies ---")

for m in movies:
    if m.genre.lower() == "action":
        print(m.movie_name)


# Highest rated movie
highest = movies[0]

for m in movies:
    if m.rating > highest.rating:
        highest = m

print("\n--- Highest Rated Movie ---")
print(highest.movie_name, highest.rating)


# Search movie by ID
search_id = int(input("\nEnter Movie ID: "))

for m in movies:
    if m.movie_id == search_id:
        print("\nMovie Found:")
        print(m.movie_id, m.movie_name, m.genre, m.rating, m.ticket_price)
        break
else:
    print("Movie Not Found")


# Average rating
total = 0

for m in movies:
    total += m.rating

average = total / len(movies)

print("\nAverage Movie Rating:", round(average, 2))


# Ticket price greater than 300
print("\n--- Movies with Ticket Price Greater Than 300 ---")

for m in movies:
    if m.ticket_price > 300:
        print(m.movie_name, m.ticket_price)