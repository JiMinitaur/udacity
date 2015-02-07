from movies import Movie

toystory = Movie({
    'title' : "Toy Story",
    'story' :
"""Adults cry with their children, as inanimate
 objects experience love, adventure, and heartbreak.
""",
    'poster' : "poster link",
    'trailer' : "video link"
    })

print(Movie.list_props())

#test canonical property id
print(toystory.storyline)

#Test alias property id
print(toystory.trailer)
