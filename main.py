from reports import show_users
from importer import UserImporter, BookImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter, AuthorImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation


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
    # show_books()
    # print("#" * 79)


if __name__ == '__main__':
    # create_tables()
    # load_data()
    show_data()
