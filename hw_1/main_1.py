#1####################################################
class Animal:
    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age

    def make_sounds(self, sound: str):
        print(f"Animal {self.type} {self.name} make sounds '{sound}'")


example = Animal(name="Bobik", type="dog", age="5")
example.make_sounds("gav-gav")

#2####################################################

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
        '''
        Метод загрузки меню
        :return:
        '''
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

#3####################################################

class PassengerPlane:
    def __init__(self, manufacturer: str, model: str, capacity: int, altitude: float, speed: float):
        '''
        Конструктор

        :param manufacturer:
        :param model:
        :param capacity:
        :param altitude:
        :param speed:
        '''
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.altitude = altitude
        self.speed = speed

    def takeoff(self):
        '''
        Метод взлета самолета
        :return:
        '''
        print(f"Самолет взлетел")

    def landing(self):
        '''
        Метод посадки самолета
        :return:
        '''
        print(f"Самолет приземлился")

    def altitude_change(self):
        '''
        Метод изменения высоты
        :param altitude:
        :return:
        '''
        self.altitude = float(input("Укажите текущую высоту >>"))

    def speed_change(self):
        '''
        Метод изменения скорости
        :param speed:
        :return:
        '''
        self.speed = float(input("Укажите текущую скорость >>"))

    def airplane_info(self):
        '''
        Метод выводы информации о самолете
        :return:
        '''
        print(f"Самолет компании '{self.manufacturer}'\n"
              f" Модель: {self.model}\n"
              f" Вместимость: {self.capacity}\n"
              f" Высота: {self.altitude}\n"
              f" Скорость: {self.speed}")

    def load_navigation(self):
        '''
        Метод загрузки навигации
        :return:
        '''
        print(f"\nМеню действий: 1 - Инфо о самолете | 2 - Изменить высоту | 3 - Изменить скорость"
              f"\n| 4 - Сообщение о взлете | 5 - Сообщение о посадке | 6 - Выход")


class Program:
    @staticmethod
    def main():
        example = PassengerPlane(manufacturer="Sukhoi", model="Superjet 100",
                                 capacity=98, altitude=0, speed=0)
        while True:
            PassengerPlane.load_navigation(self=None)
            try:
                user_select = int(input("Укажите пункт меню: "))
            except ValueError:
                print("Введите число")
            if 4 <= user_select <= 1:
                print("Введите число от 1 до 4")
            match user_select:
                case 1:
                    example.airplane_info()
                case 2:
                    example.altitude_change()
                case 3:
                    example.speed_change()
                case 4:
                    if example.altitude > 0:
                        example.takeoff()
                    else:
                        print("Наберите высоту")
                case 5:
                    if example.altitude == 0:
                        example.landing()
                    else:
                        print("Снизьте высоту")
                case 6:
                    if example.altitude != 0 or example.speed != 0:
                        print("Нельзя выйти на ходу! Снизьте скорость и высоту до 0!")
                    else:
                        break

Program.main()

#4##################################################################
class MusicAlbum:
    def __init__(self, artist: str, album: str, genre: str, tracklist: list):
        '''
        construct
        :param artist:
        :param album:
        :param genre:
        :param tracklist:
        '''
        self.artist = artist
        self.album = album
        self.genre = genre
        self.tracklist = tracklist

    def album_info(self):
        print(f"Артист: {self.artist}\n"
              f"Альбом: {self.album}\n"
              f"Жанр: {self.genre}\n"
              f"Треклист: {self.tracklist}")

    def add_track(self, track: str):
        '''
        Метод добавления трека в альбом
        :return:
        '''
        self.tracklist.append(track)
        print(f"'{track}' добавлена в альбом '{self.album}'")

    def delete_track(self, track):
        '''
        Метод удаления трека из альбома
        :param track:
        :return:
        '''
        if track in self.tracklist:
            self.tracklist.remove(track)
            print(f"Песня '{track}' удалена из альбома '{self.album}'")
        else:
            print(f"Песни '{track}' нет в альбоме '{self.album}'")

    def play_track(self, track):
        '''
        Метод воспроизведения трека
        :param track:
        :return:
        '''

        if track in self.tracklist:
            print(f"Сейчас воспроизводится '{track}' из альбома '{self.album}'")
        else:
            print(f" '{track}' нет в альбоме '{self.album}'")

    def load_player(self):
        '''
        Метод загрузки плеера
        :return:
        '''
        print(f"\nМеню действий: 1 - Инфо об альбоме | 2 - Добавить трек | 3 - Удалить трек"
              f"\n| 4 - Воспроизвести трек | 5 - Выход")

class Program:
    @staticmethod
    def main():
        example = MusicAlbum(artist="Queen", album="Innuendo",
                                     genre="rock", tracklist=['The Show Must Go On', 'Bijou'])
        while True:
            MusicAlbum.load_player(self=None)
            try:
                user_select = int(input("Укажите пункт меню: "))
            except ValueError:
                print("Введите число")
            if 5 <= user_select <= 1:
                print("Введите число от 1 до 5")
            match user_select:
                case 1:
                    example.album_info()
                case 2:
                    example.add_track(track = input("Добавить трек >>"))
                case 3:
                    example.delete_track(track = input("Удалить трек >>"))
                case 4:
                    example.play_track(track = input("Воспроизвести трек >>"))
                case 5:
                    break

Program.main()