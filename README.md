# 🎬 Movie Collection Manager

Movie Collection Manager is a Python console application designed to efficiently manage a movie collection for a cinema. This project is implemented strictly according to the provided specifications and showcases advanced Python programming skills, including object-oriented design, custom iterators, in-memory data storage using dictionaries, full type annotations, custom exception handling, and comprehensive unit testing with `pytest`.

## Features

- **Add movies:** Add new movie objects to the collection with relevant metadata such as title, director, year, genre, and duration.
- **Remove movies:** Delete movies from the collection by title.
- **Manage collection entries:** Add or remove movies within the collection dynamically.
- **Search movies:** Query the collection by multiple criteria including title, director, genre, year, and duration.
- **Iterate movies:** Traverse the movie collection using a custom iterator implemented from scratch.
- **In-memory storage:** All data is kept in application memory without any persistent storage like databases or files, strictly following assignment requirements.

## Architecture and Implementation Details

- **Object-Oriented Design:**  
  Each movie is represented by a `Movie` class instance, encapsulating all movie-related information and validation logic. The `MovieCollection` class manages all movies internally, using a Python dictionary where keys are movie titles and values are `Movie` objects. This allows O(1) average-time complexity for lookups, additions, and removals by title.

- **Custom Iterator:**  
  The `MovieCollection` class implements its own iterator protocol, allowing users to iterate over movies in a natural and Pythonic way (e.g., in a for-loop). This iterator handles internal state cleanly and respects the collection’s current state.

- **Type Annotations:**  
  All functions, methods, parameters, and return types in the project are fully annotated using Python’s type hints (PEP 484). This improves code readability, assists static analysis tools, and demonstrates adherence to modern Python best practices.

- **Exception Handling:**  
  Two custom exception classes—`DuplicateMovieError` and `MovieNotFoundError`—are defined and used consistently to signal error conditions such as attempting to add a movie that already exists or trying to remove/find a movie that is not in the collection. This approach makes the code robust and the errors explicit and easy to handle.

- **Testing:**  
  The entire functionality is covered by unit tests written with `pytest`. Tests verify successful additions, removals, searching, iteration behavior, and proper raising of custom exceptions on edge cases. Running tests is straightforward and ensures code reliability and future maintainability.

## Usage and Testing

To run the tests, first install dependencies (only `pytest` is required):

```bash
pip install -r requirements.txt