class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self, publication_type='publication', author_type='Author'):
        return f"Name of {publication_type}: {self.title}\n{author_type} of this {publication_type} is {self.author}\nYear: {self.year}\n"

    def __str__(self):
        return self.get_info()


class Book(Publication):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self, publication_type='book', author_type='Author'):
        return f"{super().get_info(publication_type, author_type)}Genre: {self.genre}\n"

    def __str__(self):
        return self.get_info()


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def get_info(self, publication_type='magazine', author_type='General editor'):
        return f"{super().get_info(publication_type, author_type)}issue_number: {self.issue_number}\n"

    def __str__(self):
        return self.get_info()


class Newspaper(Publication):
    def __init__(self, title, author, year, publisher):
        super().__init__(title, author, year)
        self.publisher = publisher

    def get_info(self, publication_type='newspaper', author_type='General editor'):
        return f"{super().get_info(publication_type, author_type)}Publisher: {self.publisher}\n"

    def __str__(self):
        return self.get_info()


if __name__ == "__main__":

    the_shining = Book("The Shining", "Stephen King", "1977", "horror")
    print(the_shining)

    the_call_of_cthulhu = Book("The Call of Cthulhu", "Howard Lovecraft", "1928", "horror")
    print(the_call_of_cthulhu)

    the_new_york_times = Newspaper("The New York Times", "Joseph Kahn", "1851 - present days", "A.G. Sulzberger")
    print(the_new_york_times)

    the_washington_post = Newspaper("The Washington Post", "Sally Streff Buzbee", "1877 - present days", "Frederick Joseph Ryan Jr.")
    print(the_washington_post)

    maxim = Magazine("Maxim", "Joe Levy", "1995 (UK) 1998 (US) - present days", "28")
    print(maxim)

    maxim = Publication("Maxim", "Joe Levy", "1995 (UK) 1998 (US) - present days")
    print(maxim)
