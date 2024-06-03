from __future__ import annotations

class Car:
    def __init__(self, brand: str, model: str, year:int, price: float, is_stock: str):
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
                f'Статус: {self.__is_stock}\n')

class Salesperson:
    def __init__(self, name, experience, sold_auto: list[Car] = None):
        self.__name = name
        self.__experience = experience
        self.__sold_auto = sold_auto

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_experience(self): return self.__experience
    def set_experience(self, experience): self.__experience = experience

    def get_sold_auto(self): return ('\n '.join(str(i) for i in self.__sold_auto))
    def set_sold_auto(self, sold_auto): self.__sold_auto = sold_auto

    def add_sold_car(self, sold_auto: Car):
        if not sold_auto in self.__sold_auto:
            self.__sold_auto.append(sold_auto)

    def remove_sold_car(self, sold_auto: Car):
        if sold_auto in self.__sold_auto:
            self.__sold_auto.remove(sold_auto)

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Опыт: {self.__experience}\n'
                f'Проданные авто: {self.get_sold_auto()}\n')

class Customer:
    def __init__(self, name: str, phone: int, email: str, purchase_auto: list[Car] = None):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__purchase_auto = purchase_auto

    def get_name(self): return self.__name
    def set_name(self, name): self.__name = name

    def get_phone(self): return self.__phone
    def set_phone(self, phone): self.__phone = phone

    def get_phone(self): return self.__email
    def set_phone(self, email): self.__email = email

    def get_purchase_auto(self): return ('\n '.join(str(i) for i in self.__purchase_auto))
    def set_purchase_auto(self, purchase_auto): self.__purchase_auto = purchase_auto

    def add_purchase_auto(self, purchase_auto: Car):
        if purchase_auto not in self.__purchase_auto:
            self.__purchase_auto.append(purchase_auto)

    def remove_purchase_auto(self, purchase_auto: Car):
        if purchase_auto in self.__purchase_auto:
            self.__purchase_auto.remove(purchase_auto)

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Телефон: {self.__phone}\n'
                f'Email: {self.__email}\n'
                f'Купленые авто: {self.get_purchase_auto()}\n')


class Dealership:
    def __init__(self, list_cars: list[Car] = None, list_customer: list[Customer] = None,
                 list_salesperson: list[Salesperson] = None):


        self.__list_cars = list_cars
        self.__list_customer = list_customer
        self.__list_salesperson = list_salesperson


    def get_list_cars(self):
        return ('\n '.join(str(i) for i in self.__list_cars))

    def set_list_cars(self, list_cars):
        self.__list_cars = list_cars

    def get_list_customer(self):
        return ('\n '.join(str(i) for i in self.__list_customer))

    def set_list_customer(self, list_customer):
        self.__list_customer = list_customer

    def get_list_salesperson(self):
        return ('\n '.join(str(i) for i in self.__list_salesperson))

    def set_list_salesperson(self, list_salesperson):
        self.__list_salesperson = list_salesperson

    def add_car_is_stock(self, car: Car):
        if car not in self.__list_cars:
            self.__list_cars.append(car)

    def remove_car_is_stock(self, car: Car):
        if car in self.__list_cars:
            self.__list_cars.remove(car)

    def add_salesperson(self, salesperson: Salesperson):
        if salesperson not in self.__list_salesperson:
            self.__salespeople.append(salesperson)

    def remove_salesperson(self, salesperson: Salesperson):
        if salesperson in self.__list_salesperson:
            self.__salespeople.remove(salesperson)

    def add_customer(self, customer: Customer):
        if customer in self.__list_customer:
            self.__list_customer.append(customer)

    def sale_car(self, car:Car, salesperson: Salesperson, customer: Customer):
        if car in self.__list_cars:
            car.set_is_stock("Нет в наличии")
            customer.add_purchase_auto(car)
            salesperson.add_sold_car(car)

    def __str__(self):
        return (f"Список продавцов: {self.get_list_salesperson()}\n"
                f"Список покупателей: {self.get_list_customer()}\n"
                f"Список авто: \n{self.get_list_cars()}\n")

class Program:

    @staticmethod
    def main():
        example_car = Car("Kia", "Magentis", 2004, 950000, "В наличии")
        example_customer = Customer("Вася", 89123456789, "email@mail.il", [example_car])
        example_salesperson = Salesperson("Игорь", 12, [example_car])
        example_dilership = Dealership([example_car], [example_customer], [example_salesperson])

        example_customer.add_purchase_auto(example_car)
        example_dilership.sale_car(example_car, example_salesperson, example_customer)

        print(example_car)
        print(example_salesperson)
        print(example_customer)
        print(example_dilership)


Program.main()
