from typing import Iterator, Dict, List
from movie import Movie
from exceptions import DuplicateMovieError, MovieNotFoundError


class MovieCollectionIterator:
    def __init__(self, movies: Dict[str, Movie]) -> None:
        self._movies = list(movies.values())
        self._index = 0

    def __iter__(self) -> 'MovieCollectionIterator':
        return self

    def __next__(self) -> Movie:
        if self._index >= len(self._movies):
            raise StopIteration
        movie = self._movies[self._index]
        self._index += 1
        return movie


class MovieCollection:
    def __init__(self) -> None:
        self._movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        if movie.title in self._movies:
            raise DuplicateMovieError(f"Movie '{movie.title}' already exists.")
        self._movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title not in self._movies:
            raise MovieNotFoundError(f"Movie '{title}' not found.")
        del self._movies[title]

    def get_movie(self, title: str) -> Movie:
        if title not in self._movies:
            raise MovieNotFoundError(f"Movie '{title}' not found.")
        return self._movies[title]

    def search_movies(self, **criteria) -> List[Movie]:
        return [movie for movie in self._movies.values() if movie.matches(**criteria)]

    def __iter__(self) -> Iterator[Movie]:
        return MovieCollectionIterator(self._movies)

    def __len__(self) -> int:
        return len(self._movies)