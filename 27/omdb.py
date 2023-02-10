import json
import re
from typing import cast, Optional, Dict, Any


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = list()
    for file in files:
        with open(file, "r") as file:
            movies.append(json.loads(file.read()))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "comedy" in movie["Genre"].lower():
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    movie_with_most_nominations = None
    for movie in movies:
        if not movie_with_most_nominations or (
            _get_nominations(movie) > _get_nominations(movie_with_most_nominations)
        ):
            movie_with_most_nominations = movie
    return movie_with_most_nominations["Title"]  # type: ignore


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_movie = None
    for movie in movies:
        if not longest_movie or (_get_runtime(movie) > _get_runtime(longest_movie)):
            longest_movie = movie
    return longest_movie["Title"]  # type: ignore


def _get_nominations(movie):
    return sum(
        [int(nom) for nom in re.findall(r"(\d+(?!\d*\s*win))", movie.get("Awards", ""))]
    )


def _get_runtime(movie):
    return int(re.search(r"(\d+)", movie["Runtime"]).group(1))
