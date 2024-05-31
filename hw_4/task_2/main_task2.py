from __future__ import annotations

class Library:
    def __init__(self, library_name: str, address: str, list_books: list[Book] = None,
                 list_employee: list[Employee] = None):
        self.__library_name = library_name
        self.__address = address
        if list_books is None:
            self.__list_books = []
        else:
            self.__list_books = list_books
        if list_employee is None:
            self.__list_employee = []
        else:
            self.__list_employee = list_employee

    def get_name_library(self):
        return self.__library_name

    def set_library_name(self, library_name):
        self.__library_name = library_name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_list_book(self):
        return self.__list_book

    def set_list_book(self, list_book):
        self.__list_book = list_book

    def get_list_employee(self):
        return self.__list_employee

    def set_list_employee(self, list_employee):
        self.__list_employee = list_employee

    def add_book(self, book: Book):
        if book not in self.__list_books:
            self.__list_books.append(book)

    def remove_book(self, book: Book):
        if  book in self.__list_books:
            self.__list_books.remove(book)

    def add_employee(self, employee: Employee):
        if not employee in self.__list_employee:
            self.__list_employee.append(employee)

    def remove_employee(self, employee: Employee):
        if employee in self.__list_employee:
            self.__list_employee.remove(employee)


    def __str__(self):
        return (f"Название библиотеки: {self.__library_name}\n"
                f"Адрес: {self.__address}\n"
                f"Список книг: {self.__list_book}\n"
                f"Список сотрудников: {self.__list_employee}\n")



class Book:
    def __init__(self, book_name:str, author: str,
                 year_publication: int, id: int, list_genre: list[Genre] = None):
        self.__book_name = book_name
        self.__author = author
        self.__year_publication = year_publication
        if list_genre is None:
            self.__list_genre = []
        else:
            self.__list_genre = list_genre
        self.__id = id

    def get_book_name(self):
        return self.__book_name
    def set_book_name(self, book_name):
        self.__book_name = book_name

    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author

    def get_year_publication(self):
        return self.__year_publication
    def set_year_publication(self, year_publication):
        self.__year_publication = year_publication

    def get_genres(self):
        return self.__list_genre

    def set_genres(self, list_genre):
        self.__list_genre = list_genre

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def add_genre(self, genre: Genre):
        if not genre in self.__list_genre:
            self.__list_genre.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__list_genre:
            self.__list_genre.remove(genre)


    def __str__(self):
        return (f"Название книги: {self.__book_name}\n"
                f"Автор: {self.__author}\n"
                f"Год издания: {self.__year_publication}, ID - {self.__id}\n"
                f"Список жанров: {self.__list_genre}\n")

class Genre:
    def __init__(self, name_genre: str, description_genre: str):
        self.__name_genre = name_genre
        self.__description_genre = description_genre

    def get_name_genre(self):
        return self.__name_genre

    def set_name_genre(self, name_genre):
        self.__name_genre = name_genre

    def get_description_genre(self):
        return self.__description_genre

    def set_description_genre(self, description_genre):
        self.__description_genre = description_genre



    def __str__(self):
        return (f"Название жанра: {self.__name_genre}\n"
                f"Описание жанра: {self.__description_genre}\n")

class Employee:
    def __init__(self, employee_name: str, id: int, position: str,
                 contact_info: list[ContactInfo] = None):
        self.__employee_name = employee_name
        self.__id = id
        self.__position = position
        if contact_info is None:
            self.__contact_info = []
        else:
            self.__contact_info = contact_info

    def get_employee_name(self):
        return self.__employee_name

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def add_contact_info(self, contact_info: ContactInfo):
        if not contact_info in self.__contact_info:
            self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info: ContactInfo):
        if contact_info in self.__contact_info:
            self.__contact_info.remove(contact_info)

    def __str__(self):
        return (f"Имя сотрудника: {self.__employee_name}\n"
                f"Должность: {self.__position}\n"
                f"ИД: {self.__id}\n"
                f"Контакты: {self.__contact_info}\n")

class ContactInfo:
    def __init__(self, type: str, value:str ):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return (f"Тип контакта: {self.__type}\n"
                f"Значение контакта: {self.__value}\n")
