import webbrowser


# defining new class which provides a way to store movie related information
class Movie():

    # creating space in memory to store movie title, poster & trailer
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        # argument to __init__ funciton to initialize movie variables
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method to play the youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
