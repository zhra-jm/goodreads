# goodreads
simulation of the site goodreads which is a platform that people add books to shelves, write comments about book and change book status. 

## Build With
* mysql

* python

## How To Use

* at first you should install virtualenv 

```apt-get install python3-virtualenv```

* then create a new virtual environment 

```virtualenv -p python3 venv```

* then we have to activate it

``` . venv/bin/activate```

* now we got to install the requirements

```pip install the requirements```

* first of all you have to create a file name ```utils.py``` and have to write down your database config in it:

* here is an example of how you should write a config:

```DATABASE_INFO = 'mysql://username:password@127.0.0.1:3306/goodreads'```

* to create database and load data from fixtures folder run:

```python3 main.py "create_tables"```

* if you wanna see all users datas run:

```python3 main.py "show_data" "all"```


* if you wanna see an specific user data run:


```python3 main.py "show_data" "user_data" "hossein" "654321"```

you can replace hossein with any username you want and also 654321 with any password.also one of them is enough to find user data

* if you want to get an specific bookshelf by id run:

```python3 main.py "get_bookshelf" "2"```

you can replace "2" with any bookshelf id you want

* if you wanna change the status of a book to read run:

```python3 main.py "change_reading_status" "2"```

you can replace "2" with any bookshelf id you want

* if you want to know book rates run:

```python3 main.py "show_book_rates"```

* if you want to see book shelf you can run:

```python3 main.py "show_book_shelves" "optimized"```

you can also replace "optimized" with "not optimized" to see a diffrent view with less data from book shelves.

 
 * Wish you have enjoyed that!Good Luck:D
