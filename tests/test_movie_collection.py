import pytest
from movie import Movie
from movie_collection import MovieCollection
from exceptions import DuplicateMovieError, MovieNotFoundError


@pytest.fixture
def sample_movie() -> Movie:
    return Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)


@pytest.fixture
def movie_collection(sample_movie: Movie) -> MovieCollection:
    collection = MovieCollection()
    collection.add_movie(sample_movie)
    return collection


def test_add_movie(movie_collection: MovieCollection) -> None:
    new_movie = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 169)
    movie_collection.add_movie(new_movie)
    assert movie_collection.get_movie("Interstellar") == new_movie


def test_add_duplicate_movie(movie_collection: MovieCollection, sample_movie: Movie) -> None:
    with pytest.raises(DuplicateMovieError):
        movie_collection.add_movie(sample_movie)


def test_remove_movie(movie_collection: MovieCollection) -> None:
    movie_collection.remove_movie("Inception")
    with pytest.raises(MovieNotFoundError):
        movie_collection.get_movie("Inception")


def test_remove_nonexistent_movie(movie_collection: MovieCollection) -> None:
    with pytest.raises(MovieNotFoundError):
        movie_collection.remove_movie("Avatar")


def test_get_movie(movie_collection: MovieCollection, sample_movie: Movie) -> None:
    movie = movie_collection.get_movie("Inception")
    assert movie == sample_movie


def test_get_nonexistent_movie(movie_collection: MovieCollection) -> None:
    with pytest.raises(MovieNotFoundError):
        movie_collection.get_movie("Nonexistent")


def test_search_movies_by_genre(movie_collection: MovieCollection) -> None:
    results = movie_collection.search_movies(genre="Sci-Fi")
    assert len(results) == 1
    assert results[0].title == "Inception"


def test_search_movies_by_year(movie_collection: MovieCollection) -> None:
    results = movie_collection.search_movies(year=2010)
    assert len(results) == 1
    assert results[0].title == "Inception"


def test_iterator(movie_collection: MovieCollection) -> None:
    titles = [movie.title for movie in movie_collection]
    assert titles == ["Inception"]