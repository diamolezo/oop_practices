from __future__ import annotations

class Wizard:
    def __init__(self, name: str, house: str, magic_level: int, status: bool,
                 spells: list[Spell] = None):
        self.__name = name
        self.__house = house
        self.__magic_level = magic_level
        if spells is None:
            self.__spells = []
        else:
            self.__spells = spells
        self.__status = status


    def get_name(self):
        '''возвращает имя волшебника.'''
        return self.__name

    def get_house(self):
        '''возвращает факультет волшебника.'''
        return self.__house

    def get_magic_level(self):
         '''   возвращает уровень магической силы волшебника.'''
         return self.__magic_level

    def get_spells(self):
        '''возвращает список известных заклинаний волшебника.'''
        return self.__spells

    def get_status(self):
        ''' возвращает текущий статус волшебника'''
        return self.__status

    def set_house(self, house: str):
        '''устанавливает факультет волшебника'''
        self.__house = house

    def set_magic_level(self, magic_level: int):
        '''устанавливает уровень магической силы волшебника (не должен быть отрицательным)'''
        if not isinstance(magic_level, int):
            raise TypeError("...")

        if 0 < magic_level < 10:
            self.__magic_level = magic_level

    def set_status(self, status: str):
        '''устанавливает текущий статус волшебника'''
        self.__status = status

    def add_spell(self, spell: Spell):
        '''добавляет заклинание в список известных'''
        if not isinstance(spell, Spell):
            raise TypeError("...")

        if not (spell in self.__spells):
            self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        '''удаляет заклинание из списка известных'''
        if not isinstance(spell, Spell):
            raise TypeError("...")

        if spell in self.__spells:
            self.__spells.remove(spell)

    def increase_magic_level(self, amount: int):
        '''увеличивает уровень магической силы на заданное значение (неотрицательное)'''
        if amount > 0:
            self.__magic_level += amount

    def __str__(self):
        '''возвращает строку, аккумулирующую состояние всех полей объекта'''
        return f"Волшебник {self.__name} из {self.__house}\n" \
               f"Маг. сила -  {self.__magic_level}\n" \
               f"Набор зелий - {self.__spells}\n" \
               f"Его статус - {self.__status}\n"

class Spell:
    def __init__(self, spell_name: str, spell_level: int, type_spell: str):
        self.__spell_name = spell_name
        self.__spell_level = spell_level
        self.__type_spell = type_spell

    def get_spell_name(self):
        return self.__spell_name

    def get_spell_level(self):
        return self.__spell_level

    def get_type_spell(self):
        return self.__type_spell

    def set_spell_name(self, spell_name):
        self.__spell_name = spell_name

    def set_spell_level(self, spell_level):
        if not isinstance(spell_level, int):
            raise TypeError("...")

        if 0 < spell_level < 10:
            self.__spell_level = spell_level

    def set_type_spell(self, type_spell):
        self.__type_spell = type_spell

    def __str__(self):
        return f"Зелье {self.__spell_name}\n" \
               f"Уровень сложности {self.__spell_level}\n" \
               f"Тип зелья {self.__type_spell}\n"

class Robot:
    def __init__(self, serial_number: int, model: str,
                 current_task: str, charge_level: int, is_active: bool):
        self.__serial_number = serial_number
        self.__model = model
        self.__current_task = current_task
        self.__charge_level = charge_level
        self.__is_active = is_active

    def get_serial_number(self):
        return self.__serial_number

    def set_serial_number(self, serial_number):
        if not isinstance(serial_number, int):
            raise TypeError("...")
        else:
            self.__serial_number = serial_number

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_current_task(self):
        return self.__current_task

    def set_current_task(self, task):
        self.__current_task = task

    def get_charge_level(self):
        return self.__charge_level

    def set_charge_level(self, charge):
        if not isinstance(charge, int):
            raise TypeError("...")
        else:
            self.__charge_level = charge

    def get_is_active(self):
        return self.__is_active

    def set_is_active(self, active:bool):
        if not isinstance(active, bool):
            raise TypeError("...")
        else:
            self.__is_active = active

    def __str__(self):
        '''возвращает строку, аккумулирующую состояние всех полей объекта'''
        return f"Робот номер {self.__serial_number} модель {self.__model}\n" \
               f"Тек. задача -  {self.__current_task}\n" \
               f"Уровень заряда - {self.__charge_level}\n" \
               f"Работает - {self.__is_active}\n"


class Athlete:
    def __init__(self, name:str, age:int, type_sports: str, is_active: bool,
                 list_achievements: list[Achievement] = None):
        self.__name = name
        self.__age = age
        self.__type_sports = type_sports
        self.__is_active = is_active
        if list_achievements is None:
            self.__list_achievements = []
        else:
            self.__list_achievements = list_achievements

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_is_active(self):
        return self.__is_active

    def set_is_active(self, is_active):
        self.__is_active = is_active

    def get_list_achievements(self):
        return self.__list_achievements

    def set_list_achievements(self, list_achievements):
        self.__list_achievements = list_achievements



    def add_achievement(self, achievement: Achievement):
        if not isinstance(achievement, Achievement):
            raise TypeError("...")

        if not (achievement in self.__list_achievements):
            self.__list_achievements.append(achievement)

    def remove_spell(self, achievement: Achievement):
        if not isinstance(achievement, Achievement):
            raise TypeError("...")

        if achievement in self.__list_achievements:
            self.__list_achievements.remove(achievement)

    def __str__(self):
        return f"Атлет {self.__name} возраст {self.__age}\n" \
               f"Вид спорта -  {self.__type_sports}\n" \
               f"Активен - {self.__is_active}\n" \
               f"Достижения - {self.__list_achievements}\n"

class Achievement:
    def __init__(self, name_achievement:str, level_achievement: int):
        self.__name_achievement = name_achievement
        self.__level_achievement = level_achievement


class Employee:
    def __init__(self, name: str, position: str, department: str, salary: int,
                 experience: int, list_projects: list):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__experience = experience
        self.__list_projects = list_projects

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if not isinstance(salary, int):
            raise TypeError("...")
        else:
            self.__salary = salary

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        if not isinstance(experience, int):
            raise TypeError("...")
        else:
            self.__experience = experience

    def get_list_projects(self):
        return self.__list_projects

    def set_list_projects(self, list_projects):
        self.__list_projects = list_projects

    def change_salary(self, salary):
        if not isinstance(salary, int):
            raise TypeError("...")
        else:
            self.__salary += salary

    def add_project(self, project):
        if not isinstance(project, str):
            raise TypeError("...")

        if not (project in self.__list_projects):
            self.__list_projects.append(project)

    def remove_project(self, project):
        if not isinstance(project, str):
            raise TypeError("...")

        if project in self.__list_projects:
            self.__list_projects.remove(project)

    def __str__(self):
        return f"Сотрудник {self.__name} должность {self.__position}\n" \
               f"Отдел -  {self.__department}\n" \
               f"Зарплата - {self.__salary}\n" \
               f"Стаж - {self.__experience}\n" \
               f"Проекты - {self.__list_projects}\n"


class Program:

    @staticmethod
    def main():

        #1##############################################################################
        example = Wizard(name="Tom", house="Dom", magic_level=8, spells=["противоорки", "ведьмоловка"], status=True)

        print(example)

        ##1.2##############################################################################
        example_spell = Spell(spell_name="ведьмоловка", spell_level=10, type_spell="боевое")

        print(example_spell)

        ##2###########################################################################
        example_employee = Employee(name="Tom", position="manager", department="IT",
                                    salary=70000, experience=7,list_projects=["website", "project crm"])
        print(example_employee)
        example_employee.change_salary(-30000)
        example_employee.add_project("server")
        print(example_employee)

        ##3###########################################################################
        example_robot = Robot(serial_number="777", model="Thunder", current_task="Таскает шпалы",
                              charge_level=12, is_active=True)
        print(example_robot)
        example_robot.set_current_task("Идти на зарядку")
        example_robot.set_charge_level(7)
        print(example_robot)

        ##4##############################################################################
        example_athlete = Athlete(name="Arni", age=25, type_sports="Бег", is_active=True,
                                  list_achievements=["Бегун планеты", "Чемпион мира"])

        print(example_athlete)

Program.main()