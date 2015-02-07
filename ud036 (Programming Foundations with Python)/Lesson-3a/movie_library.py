from movies import Movie
import fresh_tomatoes
import json

# Because I used a single property map for the constructor parameter,
# The constructor function can be used as the JSON processing callback.
with open("movies.json") as datafile:
    movies = json.load(datafile, object_hook=Movie)

print(movies)

fresh_tomatoes.open_movies_page(movies)
