import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)
    with open(MOVIE_DATA, "r") as f:
        movies = csv.DictReader(f)
        for movie in movies:
            if not all(
                [
                    key in movie
                    for key in [
                        "director_name",
                        "movie_title",
                        "title_year",
                        "imdb_score",
                    ]
                ]
            ):
                continue

            if not movie["title_year"].isdigit():
                continue

            year = int(movie["title_year"])
            if year < 1960:
                continue

            movies_by_director[movie["director_name"]].append(
                Movie(
                    movie["movie_title"],
                    int(movie["title_year"]),
                    float(movie["imdb_score"]),
                )
            )
    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    return round(mean([movie.score for movie in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    return sorted(
        [
            (director, calc_mean_score(movies))
            for director, movies in directors.items()
            if len(movies) >= MIN_MOVIES
        ],
        key=lambda pair: -pair[1],
    )
    pass
