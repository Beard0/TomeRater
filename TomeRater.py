#
# Program Objective:
# - Allow users to read and rate books.
DEBUG = False


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        # return email of associated user
        return self.email

    def change_email(self, address):

        if address != self.email:
            self.email = address
            print("{} email has been updated to {}.".format(self.name, self.email))

    def __repr__(self):
        count = len(self.books.keys())
        # for k in self.books.keys():
        #     count += 1
        return "User {}, email: {}, books read : {}.".format(self.name, self.email, count)

    def __eq__(self, other_user):
        return other_user.name == self.name and other_user.email == self.email

    def read_book(self, book, rating=None):
        if rating is not None:
            self.books[book] = rating
        else:
            self.books[book] = 0

        # optional book make logic to check
        # should add key:value to self.books
        # where key = book and value =rating

    def get_average_rating(self):
        avg_rate = 0
        count = 0
        for v in self.books.values():
            avg_rate += v
            count += 1
        return int(avg_rate / count)  # force integer

        # iterates through all values in self.books
        # returns average rating in dictionary


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if new_isbn:
            self.isbn = new_isbn
            print("{} ISBN has been updated to {isbn}".format(self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if rating is not None and rating in range(0, 5):
            self.ratings.append(rating)
        else:
            print("Invalid Rating, Enter 0-4")

    def __eq__(self, other):
        return other.title == self.title and other.isbn == self.isbn

    def get_average_rating(self):
        avg_rate = 0
        count = 0
        for i in self.ratings:
            avg_rate += i
            count += 1
        return avg_rate / count
        # loops through values in self.ratings and
        # calcualtes average rating

    def __hash__(self):
        # avoid TypeError unhashable type: 'list'
        # when we try to make dictionary with lists as keys
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        if author:
            self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.title)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        if subject and level:
            self.subject = subject
            self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:  # MAIN
    def __init__(self):
        self.users = {}
        # maps user email to User object
        self.books = {}
        # maps Book object to number of Users that have read it

    def create_book(self, title, isbn):  # creates new book
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):  # create new Fiction
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):  # create Non-Fiction
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):

        if email in self.users.keys():
            # if rating is not None: # might not need
            # print(self.users[email])
            self.users[email].read_book(book, rating)  # book is already passed as object of Book()
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():  # is book object in dict books
                self.books[book] += 1  # add value for read once
            elif book not in self.books.keys():  # if book object not in books dict
                self.books[book] = 1  # user read book one time



        elif email not in self.users.keys():
            return "No user with email {email}!".format(email=email)

        # retrieve user in self.users with key=email.
        # if doesnt exist "No user with email {}!"
        # if True user
        # self.users.get(user).read_book(book, rating)
        # call add_rating on book and rating
        # check if book is in self.books dict object already
        # if it is not add book(key) to self.books with value +=1
        # if book already in catalog increase value of it in self.books by 1

    def add_user(self, name, email, books=None):
        # if type(books) is list:

        user = User(name, email)
        self.users[user.email] = user  # self used if calling against object
        # print(type(self.users))
        if books is not None:
            if books is list:
                for i in books:
                    # print(i)
                    self.add_book_to_user(i, email, None)

    def print_catalog(self):
        for k in self.books.keys():
            print(k.get_title())
        # iterate through all self.books and prints them which are Book obj.

    def print_users(self):
        for v in self.users.values():
            print(v.name)

        # print self.users objects of User

    def get_most_read_book(self):
        largest_key = None
        largest_value = float("-inf")
        for key, value in self.books.items():
            if value > largest_value:
                largest_value = value
                largest_key = key
        return largest_key.get_title()
        # iterate through self.books and return book that has been read the most
        # Value is what should be checked for max

    def highest_rated_book(self):
        largest_key = 0
        for key in self.books.keys():
            if key.get_average_rating() > largest_key:
                largest_key = key.get_average_rating()
        return largest_key
        # iterate through all self.books and return book w/ highest average rating
        # check key in self.book than check book.get_average_rating() for max rating

    def most_positive_user(self):
        largest_value = 0
        user = None
        for value in self.users.values():
            if value.get_average_rating() > largest_value:
                largest_value = value.get_average_rating()
                user = value
        return user.name
        # iterate through all of the users in self.users
        # return user w/ highest average rating
        # self.users are Users()
        # call user.get_average_rating() on Users


# TOME RATER DUBUG
if DEBUG == True:
    fiction = Fiction("Moby Dick", "Dik Mob", 1234567)
    non_f = Non_Fiction("Moby Dick, True Story", "Survival on the deep blue", "hardcore", 1234567)
    max_b = User("Max B", "max_sux@a.mail.com")
    alek_r = User("Alek R", "alekr@mail.com")
    max_b.change_email("maxb@boss.com")
    moby = Book("Moby Dick", 1234561)
    moby.set_isbn(1231231)
    print(moby)
    print(max_b)
    print("**DEBUG** TOME RATER")
    Tome_Rater = TomeRater()
    book1 = Tome_Rater.create_book("Society of Mind", 12345678)
    Tome_Rater.add_user("David Marr", "david@computation.org")
    Tome_Rater.add_book_to_user(non_f, "alan@turing.com", 3)
    print(Tome_Rater)

    print(book1.title)
    print("compare", max_b == alek_r)
    print("compare", max_b == max_b)
    print(fiction)
    print(non_f.get_subject())
    print("**END DEBUG**")
    Tome_Rater.print_catalog()
