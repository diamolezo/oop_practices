class Student:
    def __init__(self, name:str, lastname:str, age:int, average_ball: float):
        self.__name = name
        self.__lastname = lastname
        self.__age = age
        self.__average_ball = average_ball

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("...")
        else:
            self.__age = age

    def get_average_ball(self):
        return self.__average_ball

    def set_average_ball(self, average_ball):
        if not isinstance(average_ball, float):
            raise TypeError("...")
        else:
            self.__average_ball = average_ball

    def __eq__(self, other):
        if self.__average_ball == other.__average_ball:
            print("Средний балл студентов равен. Верно")
        else:
            print("Средний балл студентов отличается. Неверно")

    def __ne__(self, other):
        if self.__average_ball != other.__average_ball:
            print("Средний балл студентов отличается. Верно")
        else:
            print("Средний балл студентов равен. Неверно")

    def __lt__(self, other):
        if self.__average_ball < other.__average_ball:
            print("Баллы 1-го меньше 2-го. Верно")
        else:
            print("Неверно")

    def __le__(self, other):
        if self.__average_ball <= other.__average_ball:
            print("Баллы 1-го меньше или равны 2-го. Верно")
        else:
            print("Неверно")

    def __gt__(self, other):
        if self.__average_ball > other.__average_ball:
            print("Баллы 1-го больше 2-го. Верно")
        else:
            print("Неверно")

    def __ge__(self, other):
        if self.__average_ball >= other.__average_ball:
            print("Баллы 1-го больше или равны 2-го. Верно")
        else:
            print("Неверно")

    def __str__(self):
        return f"Имя {self.__name} Фамилия {self.__lastname}\n" \
               f"Возраст -  {self.__age}\n" \
               f"Средний балл - {self.__average_ball}\n"


class Program:

    @staticmethod
    def main():

        example_tom = Student(name="Tom", lastname="Hardy", age=20, average_ball=4.8)
        print(example_tom)
        example_don = Student(name="Don", lastname="Montana", age=30, average_ball=4.7)
        print(example_don)
        example_tom.__eq__(example_don)
        example_tom.__le__(example_don)


Program.main()