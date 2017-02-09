import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)
toy_story.show_trailer()
