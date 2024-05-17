from __future__ import annotations
# class Car:
#     def __init__(self, car_make: str, model: str, year_of_manufacture: int,
#                  color_car: str, mileage: float, status_engine: bool, current_speed: int):
#         '''
#         construct
#         :param car_make:
#         :param model:
#         :param year_of_manufacture:
#         :param color_car:
#         :param mileage:
#         :param status_engine:
#         :param current_speed:
#         '''
#
#         self.car_make = car_make
#         self.model = model
#         self.year_of_manufacture = year_of_manufacture
#         self.color_car = color_car
#         self.mileage = mileage
#         self.status_engine = status_engine
#         self.current_speed = current_speed
#
#     def starting_the_engine(self):
#             self.status_engine = True
#
#     def get_status_engine(self):
#         return self.status_engine
#
#     def stopping_the_engine(self):
#         self.status_engine = False
#
#     def set_speed(self, speed: int):
#         if isinstance(speed, int):
#             self.current_speed = speed
#         else:
#             raise Exception("Введите число")
#
#     def get_current_speed(self):
#         return self.current_speed
#
#     def set_color(self, color: str):
#         if isinstance(color, str):
#             self.color_car = color
#         else:
#             raise Exception("Ошибка ввода")
#
#     def get_current_color(self):
#         return self.color_car
#
#     def get_current_mileage(self):
#         return self.mileage
#
#     def polling_status(self):
#         return self.status_engine, self.current_speed, self.mileage
#
#     def __str__(self):
#         return (f"Марка авто: {self.car_make}\n"
#               f"Модель авто: {self.model}\n"
#               f"Год выпуска: {self.year_of_manufacture}\n"
#               f"Цвет авто: {self.color_car}\n"
#               f"Пробег авто: {self.mileage}\n"
#               f"Состояние авто: {self.status_engine}\n"
#               f"Скорость авто: {self.current_speed}\n")

# class Smartphone:
#     def __init__(self, brand: str, model: str, type_os: str, hdd: int, hdd_free: int, ram: int, charge: int, status_on_off: bool):
#         self.brand = brand
#         self.model = model
#         self.type_os = type_os
#         self.hdd = hdd
#         self.hdd_free = hdd_free
#         self.ram = ram
#         self.charge = charge
#         self.status_on_off = status_on_off
#
#     def is_on_phone(self, status_on_off):
#         self.status_on_off = status_on_off
#
#     def install_os(self, os):
#         self.type_os = os
#
#     def install_programm(self, memory):
#         if memory < self.hdd_free:
#             self.hdd_free -= memory
#
#     def uninstall_programm(self, memory):
#         if (memory + self.hdd_free) < self.hdd:
#             self.hdd_free += memory
#
#     def polling_status(self):
#         return self.is_on_phone
#
#     def polling_charge(self):
#         return self.charge
#
#     def __str__(self):
#         return (f"Бренд: {self.brand}\n"
#                 f"Модель: {self.model}\n"
#                 f"ОС: {self.type_os}\n"
#                 f"Память: {self.hdd}\n"
#                 f"Свободная память: {self.hdd_free}\n"
#                 f"Оперативная память: {self.ram}\n"
#                 f"Уровень заряда: {self.charge}\n"
#                 f"Вкл/Выкл: {self.is_on_phone}\n")

# class Potions:
#     def __init__(self, name_of_potion: str, ingridients: list, difficulty_of_preparation: int,
#     effect_of_potion: str, is_cooked: bool):
#         self.name_of_potion = name_of_potion
#         self.ingridients = ingridients
#         self.difficulty_of_preparation = difficulty_of_preparation
#         self.effect_of_potion = effect_of_potion
#         self.is_cooked = is_cooked
#
#     def add_ingridient(self, ingridient):
#         self.ingridients.append(ingridient)
#
#     def del_ingridient(self, ingridient):
#         if ingridient in self.ingridients:
#             self.ingridients.remove(ingridient)
#
#     def cooking_potion(self, is_cooked):
#         if is_cooked == True:
#             self.is_cooked = is_cooked
#
#
#     def change_difficulty(self, level):
#         if 0 > level < 10 and isinstance(level, int):
#             self.difficulty_of_preparation = level
#
#     def change_effect(self, effect):
#         self.effect_of_potion = effect
#
#     def polling_potion(self):
#         return self.is_cooked
#
#     def __str__(self):
#         return (f"Название: {self.name_of_potion}\n"
#                 f"Ингридиенты: {self.ingridients}\n"
#                 f"Сложность: {self.difficulty_of_preparation}\n"
#                 f"Эффект: {self.effect_of_potion}\n"
#                 f"Готовность: {self.is_cooked}\n")

class Library:
    def __init__(self, library_name: str, address: str, list_books: list[Book] = None, list_users: list[User] = None):
        self.library_name = library_name
        self.address = address
        if list_books is None:
            self.list_books = []
        else:
            self.list_books = list_books
        if list_users is None:
            self.list_users = []
        else:
            self.list_users = list_users

    def add_book(self, book: Book):
        if book not in self.list_books:
            self.list_books.append(book)

    def remove_book(self, book: Book):
        if  book in self.list_books:
            self.list_books.remove(book)

    def register_user(self, user: User):
        if not user in self.list_users:
            self.list_users.append(user)

    def issue_book(self, book: Book, user: User):
        if book.is_stock:
            book.set_stock(False)
            book.set_current_user(user)
            user.set_user_books(book)

    def return_book(self, book: Book, user: User):
        book.set_stock(True)
        book.set_current_user(None)
        user.del_user_books(book)

    @staticmethod
    def get_books_status(self) -> str:
        return (f"Название книги: {self.book_name}\n"
                f"Автор: {self.author}\n"
                f"Наличие: {self.is_stock}\n"
                f"Текущий пользователь: {self.current_user}\n")

    @staticmethod
    def get_users_status(self) -> str:
        return (f"Имя: {self.user_name}\n"
                f"Читательский билет: {self.library_card}\n"
                f"Список книг: {self.user_books}\n")


class Book:
    def __init__(self, book_name:str, author: str, year_publication: int, genre: str,
                 current_user: User, is_stock: bool):
        self.book_name = book_name
        self.author = author
        self.year_publication = year_publication
        self.genre = genre
        self.is_stock = is_stock
        self.current_user = current_user

    def set_is_stock(self, is_stock):
        self.is_stock = is_stock

    def set_current_user(self, user):
        self.current_user = user

    def set_genre(self, genre):
        self.genre = genre

    def get_is_stock(self):
        return self.is_stock



class User:
    def __init__(self, user_name: str, library_card: int, user_books: Book):
        self.user_name = user_name
        self.library_card = library_card
        self.user_books = user_books

    def add_user_books(self, book: Book):
        if book not in self.user_books:
            self.user_books.append(book)

    def del_user_books(self, book: Book):
        if book in self.user_books:
            self.user_books.remove(book)

    def get_user_books(self):
        return self.user_books

class Program:

    @staticmethod
    def main():
        example = Library(library_name="Gorkiy", address="Port-Saida 00", list_books=None)
        example_book = Book(book_name="1984", author="Джордж Оруэлл", genre="utopia",
                            year_publication="1967", is_stock=True, current_user=None)
        example_user = User(user_name="Tom", library_card=1234, user_books=None)



##1##############################################################################
# example = Car(car_make="Honda", model="Civic", year_of_manufacture=2000,
#          color_car="red", mileage=222333, status_engine="Запущен", current_speed=65)

# example.set_speed(speed=20)
# print(example)

##2##############################################################################
# example = Smartphone(brand="Iphone", model=15, type_os="iOS",
#                      hdd=256, hdd_free=200, ram=16, charge=80, status_on_off=True)
# example.uninstall_programm(19)
# print(example)

#3##############################################################################
# example = Potions(name_of_potion="Abra", ingridients=["чеснок", "жаба"], difficulty_of_preparation=7,
#                   effect_of_potion="глюки", is_cooked=False)
# example.add_ingridient("клей")
# example.del_ingridient("жаба")
# example.cooking_potion(False)
# print(example)



Program.main()
