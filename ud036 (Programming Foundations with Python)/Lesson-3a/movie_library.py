from movies import Movie
import fresh_tomatoes
import json

with open("movies.json") as datafile:
    json_data = json.load(datafile)

print json_data

movies = []
for movie in json_data:
    movies.append(Movie(movie))

print (movie)

fresh_tomatoes.open_movies_page(movies)
