class Book:

    _title = "None"
    _author = "None"
    _release_date = None
    _number_of_page = None
    _owner = "None"

    def __init__(self, _title, _author, _release_date, _number_of_page, _owner):
        self._title = _title
        self._author = _author
        self._release_date = _release_date
        self._number_of_page = _number_of_page
        self._owner = _owner

    def new_owner(self, _new_owner):
        self._owner = _new_owner

    def print_book(self):
        quot_mark = "\""
        print(quot_mark, self._title, quot_mark, quot_mark, self._author, quot_mark, self._release_date,
              self._number_of_page, quot_mark, self._owner, quot_mark)


k1 = Book("The Godfather", "Puzo Mario", 1969, 500, "Analyst")

k1.print_book()
