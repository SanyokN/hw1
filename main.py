from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        pass


class Book(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, number_of_pages: int):
        super().__init__(title, author_or_director, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return (f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, "
                f"Number of pages: {self.number_of_pages}")


class Magazine(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, issue_number: int):
        super().__init__(title, author_or_director, year)
        self.issue_number = issue_number

    def description(self):
        return (f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, "
                f"Issue number: {self.issue_number}")


class DVD(LibraryItem):
    def __init__(self, title: str, author_or_director: str, year: int, duration: int):
        super().__init__(title, author_or_director, year)
        self.duration = duration

    def description(self):
        return (f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, "
                f"Duration: {self.duration}")


book = Book("A Tale of Two Cities", "Charles Dickens", 1859, 489)
magazine = Magazine("ADAC Motorwelt", "BCN", 1925, 72842)
dvd = DVD("Paramount Pictures presents", "Paramount Pictures", 1999, 90)
print(book.description())
print(magazine.description())
print(dvd.description())
