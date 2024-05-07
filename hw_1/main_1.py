#1
class Animal:
    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age

    def make_sounds(self, sound: str):
        print(f"Animal {self.type} {self.name} make sounds '{sound}'")


example = Animal(name="Bobik", type="dog", age="5")
example.make_sounds("gav-gav")

#2

class Book:
    def __init__(self, name: str, author: str, qty: int):
        '''
        Конструктор

        :param name:
        :param author:
        :param qty:
        '''
        self.name = name
        self.author = author
        self.qty = qty


    def output_book(self):
        '''
          Метод вывода информации о книге
        :return:
        '''

        print(f"Книга '{self.name}', автор {self.author}. В книге "
              f"{self.qty} страниц.\n")
    def open_book(self, page: int):
        '''
        Метод открытия определенной страницы книги

        :param page:
        :return:
        '''

        if page >= 1 and page <= self.qty:
            print(f"Страница {page} успешно открыта в книге '{self.name}', {self.author}\n")
        else:
            print(f"Страницы {page} нет в книге '{self.name}', {self.author}\n")

    def load_menu(self):
        print(f"Меню действий: 1 - Инфо о книге | 2 - Открыть страницу | 3 - Выход")


class Program:
    @staticmethod
    def main():
        example = Book(name="1984", author="Джордж Оруэлл", qty=288)
        while True:
            Book.load_menu(self=None)
            try:
                user_select = int(input("Укажите пункт меню: "))
            except ValueError:
                print("Введите число")
            if 3 <= user_select <= 1:
                print("Введите число от 1 до 3")
            match user_select:
                case 1:
                    example.output_book()
                case 2:
                    example.open_book(int(input("Страница >> ")))
                case 3:
                    break






Program.main()