from movies import Movie

toystory = Movie({
    'title' : "Toy Story",
    'story' :
"""Adults cry with their children, as inanimate
 objects experience love, adventure, and heartbreak.
""",
    'poster' : "http://cdnvideo.dolimg.com/cdn_assets/5670999ffe25e4bd664bc9486adef5171a494e7f.jpg",
    'trailer' : "http://youtu.be/KYz2wyBy3kc"
    })

print(Movie.list_props())

#test canonical property id
print(toystory.storyline)

#Test alias property id
print(toystory.trailer)

toystory.show_trailer()
