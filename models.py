from peewee import Model, CharField, ForeignKeyField, SmallIntegerField, TextField, DateField, \
    DateTimeField
from datetime import datetime
from playhouse.db_url import connect

database = connect('mysql://zahra:3078@127.0.0.1:3306/goodreads')


class BaseModel(Model):

    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class User(BaseModel):
    username = CharField(max_length=32)
    password = CharField(max_length=32)


class Book(BaseModel):
    name = CharField(max_length=225)
    isbn = CharField(max_length=32)


class Author(BaseModel):
    name = CharField(max_length=32)


class Shelf(BaseModel):
    name = CharField(max_length=32)
    user = ForeignKeyField(User, backref='shelves')


class BookShelf(BaseModel):
    book = ForeignKeyField(Book, backref='book_shelves')
    user = ForeignKeyField(User, backref='book_shelves')
    shelf = ForeignKeyField(Shelf, backref='book_shelves')
    rate = SmallIntegerField()
    comment = TextField()
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    create_date = DateTimeField(default=datetime.now())


class BookAuthor(BaseModel):
    author = ForeignKeyField(Author, backref='books')
    book = ForeignKeyField(Book, backref='authors')


class BookTranslator(BaseModel):
    translator = ForeignKeyField(Author, backref='translators')
    book = ForeignKeyField(Book, backref='translated_books')


class UserAuthorRelation(BaseModel):
    user = ForeignKeyField(User, backref='followed_users')
    author = ForeignKeyField(Author, backref='following_users')


class UserRelation(BaseModel):
    following = ForeignKeyField(User, backref='following')
    follower = ForeignKeyField(User, backref='follower')