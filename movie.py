from typing import List


class Movie:
    def __init__(self, title: str, director: str, year: int, genre: str, duration_minutes: int) -> None:
        self.title: str = title
        self.director: str = director
        self.year: int = year
        self.genre: str = genre
        self.duration_minutes: int = duration_minutes

    def __str__(self) -> str:
        return (f"{self.title} ({self.year}) — {self.genre}, "
                f"directed by {self.director}, {self.duration_minutes} min")

    def matches(self, **criteria) -> bool:
        """
        Allows flexible search based on keyword criteria.
        Example: matches(genre="Action", year=2020)
        """
        for key, value in criteria.items():
            if not hasattr(self, key) or getattr(self, key) != value:
                return False
        return True