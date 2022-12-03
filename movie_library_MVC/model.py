class Movie:
    def __init__(self, title, genre, producer, year, time, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title} ({self.producer})'


class MovieModel:
    def __init__(self):
        self.movies = {}

    def add_movie(self, dict_movies):
        movie = Movie(*dict_movies.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movies = self.movies[user_title]
        dict_movie = {
            'название фильма': movies.title,
            'жанр': movies.genre,
            'режиссер': movies.producer,
            'год выпуска': movies.year,
            'длительность': movies.time,
            'студия': movies.studio,
            'актеры': movies.actors
        }
        return dict_movie

    def remove_movie(self, delete_movie):
        return self.movies.pop(delete_movie)
