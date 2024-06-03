from __future__ import annotations

class Car:
    def __init__(self, brand:str, model:str, year:int, price:float, is_stock:str):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__is_stock = is_stock

    def get_brand(self): return self.__brand
    def set_brand(self, brand): self.__brand = brand

    def get_model(self): return self.__model
    def set_model(self, model): self.__model = model

    def get_year(self): return self.__year
    def set_year(self, year): self.__year = year

    def get_price(self): return self.__price
    def set_price(self, price): self.__price = price

    def get_is_stock(self): return self.__is_stock
    def set_is_stock(self, is_stock): self.__is_stock = is_stock

    def __str__(self):
        return (f'Бренд: {self.__brand}\n'
                f'Модель: {self.__model}\n'
                f'Год: {self.__year}\n'
                f'Цена: {self.__price}\n'
                f'Статус: {self.__is_status}\n')

class Salesperson:
    def __init__(self, name, experience, sold_auto: list[Car] = None):
        self.__name = name
        self.__experience = experience
        if self.__sold_auto is None:
            self.__sold_auto = []
        else:
            self.__sold_auto = sold_auto

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_experience(self): return self.__experience
    def set_experience(self, experience): self.__experience = experience

    def get_sold_auto(self): return ('\n '.join(str(i) for i in self.__sold_auto))
    def set_sold_auto(self, sold_auto): self.__sold_auto = sold_auto

    def add_sold_car(self, sold_auto: Car):
        self.__sold_auto.append(sold_auto)

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Опыт: {self.__experience}\n'
                f'Проданные авто: {self.get_sold_auto()}\n')

class Dealership:
    def __init__(self):