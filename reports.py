from models import User, Shelf, Book


def show_users():
    users = User.select()
    for user in users:
        # shelves_count = user.shelves.count()
        shelves = ', '.join([shelf.name for shelf in user.shelves])
        print(user.username, '\t', shelves, '\t', user.book_shelves.count())
