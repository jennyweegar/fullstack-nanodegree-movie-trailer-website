import fresh_tomatoes
import media

# creating a new instance/object in class Movie

# each objects data is hard coded below

big_lebowski = media.Movie("The Big Lebowski",  # instance variable example
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")


o_brother = media.Movie("O Brother, Where Art Thou?",
                        "https://upload.wikimedia.org/wikipedia/en/5/5b/O_brother_where_art_thou_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=ZSlEkPusaCc")


the_darjeeling_limited = media.Movie("The Darjeeling Limited",
                                     "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",  # NOQA
                                     "https://www.youtube.com/watch?v=aO1bYukdvLI")  # NOQA


moonrise_kingdom = media.Movie("Moonrise Kingdom",
                               "https://upload.wikimedia.org/wikipedia/en/4/4f/Moonrise_Kingdom_FilmPoster.jpeg",  # NOQA
                               "https://www.youtube.com/watch?v=7N8wkVA4_8s")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=0zFywiAh7N0")

the_royal_tenenbaums = media.Movie("The Royal Tenenbaums",
                                   "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=W5AU78dqBgE")  # NOQA

# creating the list of movies to pass to below method
movies = [big_lebowski, o_brother, the_darjeeling_limited,
          moonrise_kingdom, eternal_sunshine, the_royal_tenenbaums]
# generates webpage displaying movies
fresh_tomatoes.open_movies_page(movies)
