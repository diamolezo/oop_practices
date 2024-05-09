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

class ModelWindow:
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1960

    def __init__(self, header: str, left_up_corner: int, horizontal_size: int, vertical_size: int, window_color: str,
                 visible_invisible: str, with_without_frame: str):
        '''
        construct
        :param header:
        :param left_up_corner:
        :param horizontal_size:
        :param vertical_size:
        :param window_color:
        :param visible_invisible:
        :param with_without_frame:
        '''

        self.header = header
        self.left_up_corner = left_up_corner
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.window_color = window_color
        self.visible_invisible = visible_invisible
        self.with_without_frame = with_without_frame

    def take_left_up_corner(self, x: int, y: int):
        self.coordinate_x = x
        self.coordinate_y = y
        
    def moving_horizontally(self):
        '''
        Метод передвижения окна по горизонтали
        :return:
        '''

    def moving_vertically(self):
        '''
        Метод передвижения окна по вертикали
        :return:
        '''


    def changing_height(self, height):
        '''
        Метод изменения высоты
        :return:
        '''
        if height + self.coordinate_y < ModelWindow.SCREEN_HEIGHT:
            self.vertical_size = height
            print(f"Высота окна теперь: {self.vertical_size}\n")
        else:
            print("Размер окна больше экрана. Укажите размер меньше")

    def changing_width(self, width):
        '''
        Метод изменения ширины
        :return:
        '''
        if width + self.coordinate_x < ModelWindow.SCREEN_WIDTH:
            self.horizontal_size = width
            print(f"Ширина  окна теперь: {self.horizontal_size}\n")
        else:
            print("Размер окна больше экрана. Укажите размер меньше")

    def changing_color(self, color):
        '''
        Метод изменения цвета
        :return:
        '''
        self.window_color = color
        print(f"Цвет окна: {self.window_color}\n")

    def changing_state(self, state):
        '''
        Метод изменения состояния
        :return:
        '''
        if state == 13 or state == 31:
            self.visible_invisible = "Видимое"
            self.with_without_frame = "С рамкой"
        elif state == 14 or state == 41:
            self.visible_invisible = "Видимое"
            self.with_without_frame = "Без рамки"
        elif state == 23 or state == 32:
            self.visible_invisible = "Не видимое"
            self.with_without_frame = "С рамкой"
        elif state == 24 or state == 42:
            self.visible_invisible = "Не видимое"
            self.with_without_frame = "Без рамки"
        else:
            print("Такое состояние невозможно\n")

        print(f"Состояние видимости: {self.visible_invisible}\n"
              f"Состояние рамки: {self.with_without_frame}\n")


    def polling_state(self):
        '''
        Метод опроса состояния
        :return:
        '''

    @staticmethod
    def operation_to_windows():
        example_windows = ModelWindow(header="Title", left_up_corner=10, horizontal_size=100, vertical_size=200,
                                      window_color="red", visible_invisible="visible", with_without_frame="with frame")

        while True:

            print(f"\nМеню действий:\n"
                  f"0 - Указать координаты левого верхнего угла окна | \n"
                  f"1 - Передвинуть по горизонтали | \n"
                  f"2 - Передвинуть по вертикали |\n"
                  f"3 - Изменить высоту окна |\n"
                  f"4 - Изменить ширину окна |\n"
                  f"5 - Изменить цвет |\n"
                  f"6 - Видимость/Невидимость и С рамкой/Без рамки|\n"
                  f"7 - Выход")

            menu_select = int(input("Укажите пункт меню: "))

            if 8 <= menu_select <= 1:
                print("Введите число от 1 до 8")
            match menu_select:
                case 0:
                    x = int(input("Укажите x: "))
                    y = int(input("Укажите y: "))
                    example_windows.take_left_up_corner(x, y)
                case 1:
                    pass
                case 2:
                    pass

                case 3:
                    height = int(input("Укажите высоту: "))
                    example_windows.changing_height(height)

                case 4:
                    width = int(input("Укажите ширину: "))
                    example_windows.changing_width(width)

                case 5:
                    color = int(input("Укажите цвет: "))
                    example_windows.changing_color(color)

                case 6:
                    state =int(input("Настройки рамки и видимости:\n"
                                        "1 - Видимое окно\n"
                                        "2 - Не видимое окно\n"
                                        "3 - С рамкой\n"
                                        "4 - Без рамки\n"
                                        "Например: 24 (это будет Не видимое окно без рамки)\n"
                                     "Укажите значение: "))
                    example_windows.changing_state(state)

                case 7:
                    break





class Program:

    @staticmethod
    def load_menu():
        '''
        Метод загрузки меню
        :return:
        '''
        print(f"\nПрограммы:\n"
              f"Пациенты: 1 - Записаться на прием | \n"
              f"Туристы: 2 - Посетить место |\n"
              f"Окна: 3 - Операции над окнами |\n"
              f"\n| 4 - Воспроизвести трек |\n"
              f" | 5 - Выход")

    @staticmethod
    def main():

        example_patient = Patient(fio="Иванов Петр Сидорович", age="59", current_disease="Диабет")
        example_tourist = TouristSpot(name_place="Колизей", country="Италии", type_of_attraction="историческую")
        example_windows = ModelWindow(header="Title", left_up_corner=10, horizontal_size=100, vertical_size=200,
                                      window_color="red", visible_invisible="visible", with_without_frame="with frame")

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
                    example_windows.operation_to_windows()
                case 4:
                    pass
                case 5:
                    break

Program.main()