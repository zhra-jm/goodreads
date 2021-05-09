from reports import show_users, show_books
from importer import UserImporter, BookImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter, AuthorImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation
from peewee import fn


def create_tables():
    database.create_tables(
        [User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, UserRelation]
    )


def load_data():
    importer_classes = [UserImporter, BookImporter, AuthorImporter,
                        BookAuthorImporter, ShelfImporter, BookShelfImporter]

    for _class in importer_classes:
        print(_class.load())


def show_data():
    print("#" * 79)
    show_users()
    print("#" * 79)
    show_books()
    print("#" * 79)


def show_user_data(username='hosein', password='654321'):
    user = User.authenticate(username, password)
    if user is None:
        print('user not found!')
        return
    print(f'username : {user.username}')

    print('\nBook shelves: ')
    for shelf in user.shelves:
        print(f"\t{shelf.name}: {shelf.book_shelves.count()}")

    print('\nBooks:')
    for book_shelf_instance in user.book_shelves:
        print(f'\t{book_shelf_instance.book.id}\t{book_shelf_instance.book.name}')

    # book = Book.get_by_id(3)
    # read_shelf = user.shelves.where(Shelf.name == Shelf.READ)
    # new_book_shelf = BookShelf.create(
    #     book=book, user=user, shelf=read_shelf, rate='3',
    #     comment='not a bad book',start_date='2020-10-05'
    # )


def show_book_rates():
    query = BookShelf.select(
        BookShelf.book,
        fn.SUM(BookShelf.rate).alias('rate_sum'),
        fn.COUNT(BookShelf.rate).alias('rate_count')
    ).group_by(BookShelf.book)
    for q in query:
        print(q.book_id, q.rate_sum / q.rate_count)


def show_book_shelves():
    query = BookShelf.select(
        BookShelf.user,
        BookShelf.shelf,
        fn.count(BookShelf.book).alias('book_count')
    ).group_by(BookShelf.shelf)

    for q in query:
        print(q.user.username, q.shelf.name, q.book_count)


if __name__ == '__main__':
    # create_tables()
    # load_data()
    # show_data()
    # show_user_data('hosein', '654321')
    # show_user_data('zhra')
    # show_user_data()
    # bs = BookShelf.get_by_id(2)
    # bs.change_to_read()
    show_book_rates()
    # show_book_shelves()
