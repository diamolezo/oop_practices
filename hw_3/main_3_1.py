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

        if not (spell in self.__spells):
            self.__spells.remove(spell)

    def increase_magic_level(self, amount: int):
        '''увеличивает уровень магической силы на заданное значение (неотрицательное)'''
        if amount > 0:
            self.__magic_level += amount

    def __str__(self):
        '''возвращает строку, аккумулирующую состояние всех полей объекта'''
        return f"Волшебник {self.__name} из {self.__house}" \
               f"Маг. сила -  {self.__magic_level}" \
               f"Набор заклинаний - {self.__spells}" \
               f"Его статус - {self.__status}"

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
        return f"Зелье {self.__spell_name}" \
               f"Уровень сложности {self.__spell_level}" \
               f"Тип зелья {self.__type_spell}"
