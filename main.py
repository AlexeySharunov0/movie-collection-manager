from movie import Movie
from movie_collection import MovieCollection
from exceptions import DuplicateMovieError, MovieNotFoundError


def print_menu() -> None:
    print("\nMovie Collection Manager")
    print("1. Add movie")
    print("2. Remove movie")
    print("3. View all movies")
    print("4. Search movies")
    print("5. Get movie by title")
    print("6. Exit")


def prompt_movie() -> Movie:
    title = input("Title: ")
    director = input("Director: ")
    year = int(input("Year: "))
    genre = input("Genre: ")
    duration = int(input("Duration (minutes): "))
    return Movie(title, director, year, genre, duration)


def main() -> None:
    collection = MovieCollection()

    while True:
        print_menu()
        choice = input("Select option: ")

        if choice == "1":
            try:
                movie = prompt_movie()
                collection.add_movie(movie)
                print(f"Added movie: {movie}")
            except DuplicateMovieError as e:
                print(e)

        elif choice == "2":
            title = input("Enter title to remove: ")
            try:
                collection.remove_movie(title)
                print(f"Removed movie '{title}'")
            except MovieNotFoundError as e:
                print(e)

        elif choice == "3":
            print("\nAll movies:")
            for movie in collection:
                print(f"- {movie}")

        elif choice == "4":
            key = input("Enter field to search by (e.g., genre, year): ")
            value = input("Enter value: ")
            if key == "year" or key == "duration_minutes":
                value = int(value)
            results = collection.search_movies(**{key: value})
            print(f"Found {len(results)} result(s):")
            for movie in results:
                print(f"- {movie}")

        elif choice == "5":
            title = input("Enter title: ")
            try:
                movie = collection.get_movie(title)
                print(movie)
            except MovieNotFoundError as e:
                print(e)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()