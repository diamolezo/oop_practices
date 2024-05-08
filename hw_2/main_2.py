import datetime

#____1_____###############################################################################
class Patient:
    def __init__(self, fio: str, age: int, current_disease: str):
        '''
        construct
        :param fio:
        :param age:
        :param current_disease:
        '''
        self.fio = fio
        self.age = age
        self.current_disease = current_disease

    def make_an_appointment(self, date: str, time: str):
        print(f"Пациент {self.fio}, возраст {self.age} лет, с текущим заболеванием"
              f"{self.current_disease} записан на прием {date} в {time}")


#____2_____###############################################################################
class TouristSpot:
    def __init__(self, name_place: str, country: int, type_of_attraction: str):
        '''
        construct
        :param name_place:
        :param country:
        :param type_of_attraction:
        '''
        self.name_place = name_place
        self.country = country
        self.type_of_attraction = type_of_attraction

    def visit_place(self, name_tourist: str):
        print(f"{name_tourist} посетил {self.type_of_attraction} достопримечательность '{self.name_place}' в {self.country}")


#____3_____###############################################################################


class Program:

    @staticmethod
    def load_menu():
        '''
        Метод загрузки меню
        :return:
        '''
        print(f"\nМеню действий:\n"
              f"Пациенты: 1 - Записаться на прием | \n"
              f"Туристы: 2 - Посетить место |\n"
              f"Модели: 3 - Удалить трек"
              f"\n| 4 - Воспроизвести трек | 5 - Выход")

    @staticmethod
    def main():
        example_patient = Patient(fio="Иванов Петр Сидорович", age="59", current_disease="Диабет")
        example_tourist = TouristSpot(name_place="Колизей", country="Италии", type_of_attraction="историческую")
        while True:

            Program.load_menu()
            user_select = int(input("Укажите пункт меню: "))

            if 5 <= user_select <= 1:
                print("Введите число от 1 до 5")
            match user_select:
                case 1:
                    date = input("Введите дату в формате ДД-ММ-ГГГГ ")
                    time = input("Введите время в формате ЧЧ-ММ ")

                    example_patient.make_an_appointment(date, time)
                case 2:
                    name_tourist = input("Ваше имя? >> ")

                    example_tourist.visit_place(name_tourist)
                case 3:
                    example.delete_track(track = input("Удалить трек >>"))
                case 4:
                    example.play_track(track = input("Воспроизвести трек >>"))
                case 5:
                    break

Program.main()