import source
import sys

from models import BookShelf

if __name__ == '__main__':
    if sys.argv[1] == "create_tables":
        source.create_tables()
    elif sys.argv[1] == "load_data":
        source.load_data()
    elif sys.argv[1] == "show_data":
        if sys.argv[2] == "all":
            source.show_data()
        elif sys.argv[2] == "user_data":
            source.show_user_data(sys.argv[3], sys.argv[4])
        else:
            print("you entered wrong key.plz try again")
    elif sys.argv[1] == "get_bookshelf":
        BookShelf.get_by_id(sys.argv[2])
    elif sys.argv[1] == "change_reading_status":
        bs = BookShelf.get_by_id(sys.argv[2])
        bs.change_to_read()
    elif sys.argv[1] == "show_book_rates":
        source.show_book_rates()
    elif sys.argv[1] == "show_book_shelves":
        if sys.argv[2] == "optimized":
            source.show_all_book_shelves_optimized()
        elif sys.argv[2] == "not optimized":
            source.show_book_shelves()
        else:
            print("you entered wrong key.plz try again")
    else:
        print("you entered wrong key.plz try again")
