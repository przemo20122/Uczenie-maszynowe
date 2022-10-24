import Library
class Book:
    def __init__(self, librabry, publication_date, author_name, author_surname, number_of_pages):
        self.librabry = librabry
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Ksiazka:{}, {}, {}, {}, {}".format(self.librabry, self.publication_date, self.author_name,
                                                   self.author_surname, self.number_of_pages)
