import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku_id):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youku_id = trailer_youku_id

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
