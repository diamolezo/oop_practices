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
        self.name = name
        self.author = author
        self.qty = qty
    def open_book(self, page: int):

        if self.qty >= 1 and self.qty <= page:
            print(f"Page {page} open in book '{self.name}', {self.author}")
        else:
            print(f"Page {page} not open in book '{self.name}', {self.author}")


class Program:
    @staticmethod
    def main():
        example = Book(name="1984", author="Джордж Оруэлл", qty=288)
        example.open_book(int(input("Page >> ")))

Program.main()