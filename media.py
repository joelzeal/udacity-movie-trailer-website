# import webbrowser module
import webbrowser


class Movie():

    """definition of the class movie"""
    # define constructor
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, movie_actor,
                 movie_year):
        """Define constructor"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actor = movie_actor
        self.year = movie_year
