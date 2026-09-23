"""============================================================
ASSIGNMENT 5 – BOOK MANAGEMENT SYSTEM
=====================================

Create a Book class inside:

models/book.py

ATTRIBUTES:

* book_id
* book_name
* author
* price

TASKS:

1. Take details of 5 books from the user.
2. Create Book objects.
3. Store all Book objects in a list.
4. Display all books.
5. Search a book using Book Id.
6. Display all books written by a particular author.
7. Display books whose price is greater than 500.
8. Find the most expensive book.
9. Calculate average price of all books.

SAMPLE INPUT:

101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

EXPECTED OUTPUT:

All Books:
101 Java Programming James 650
102 Python Basics Mark 550
103 MySQL Guide John 450
104 Advanced Java James 800
105 DSA in Python Robert 700

Books by James:
101 Java Programming 650
104 Advanced Java 800

Books with price greater than 500:
Java Programming
Python Basics
Advanced Java
DSA in Python

Most Expensive Book:
Advanced Java = 800

Average Price:
630"""
class Book:

    def __init__(self, book_id, book_name, author, price):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.price = price

    def display(self):
        print(self.book_id, self.book_name, self.author, self.price)


# Create list
books = []

# Take details of 5 books
for i in range(5):
    print("\nEnter details of Book", i + 1)

    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    price = int(input("Enter Price: "))

    book = Book(book_id, book_name, author, price)
    books.append(book)


# Display all books
print("\nAll Books:")

for book in books:
    book.display()


# Search book by ID
book_id = int(input("\nEnter Book ID to search: "))

for book in books:
    if book.book_id == book_id:
        print("Book Found:")
        book.display()
        break
else:
    print("Book not found")


# Books by particular author
author_name = input("\nEnter Author Name: ")

print("\nBooks by", author_name + ":")

for book in books:
    if book.author.lower() == author_name.lower():
        print(book.book_id, book.book_name, book.price)


# Books with price greater than 500
print("\nBooks with price greater than 500:")

for book in books:
    if book.price > 500:
        print(book.book_name)


# Most expensive book
expensive = books[0]

for book in books:
    if book.price > expensive.price:
        expensive = book

print("\nMost Expensive Book:")
print(expensive.book_name, "=", expensive.price)


# Average price
total = 0

for book in books:
    total += book.price

average = total / len(books)

print("\nAverage Price:", average)