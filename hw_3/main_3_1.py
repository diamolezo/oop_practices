from __future__ import annotations

class Wizard:
    def __init__(self, name: str, house: str, magic_level: int, status: bool,
                 spells: list[Spell] = None):
        self.name = name
        self.house = house
        self.magic_level = magic_level
        if spells is None:
            self.spells = []
        else:
            self.spells = spells
        self.status = status


    def get_name(self):
        '''возвращает имя волшебника.'''
        return self.name

    def get_house(self):
        '''возвращает факультет волшебника.'''
        return self.house

    def get_magic_level(self):
         '''   возвращает уровень магической силы волшебника.'''
         return self.magic_level

    def get_spells(self):
        '''возвращает список известных заклинаний волшебника.'''
        return self.spells

    def get_status(self):
        ''' возвращает текущий статус волшебника'''
        return self.status

    def set_house(self, house: str):
        '''устанавливает факультет волшебника'''
        self.house = house

    def set_magic_level(self, magic_level: int):
        '''устанавливает уровень магической силы волшебника (не должен быть отрицательным)'''
        self.magic_level = magic_level

    def set_status(self, status: str):
        '''устанавливает текущий статус волшебника'''
        self.status = status

    def add_spell(self, spell: Spell):
        '''добавляет заклинание в список известных'''
        pass

    def remove_spell(spell: Spell):
        '''удаляет заклинание из списка известных'''
        pass

    def increase_magic_level(self, amount: int):
        '''увеличивает уровень магической силы на заданное значение (неотрицательное)'''
        if amount > 0:
            self.magic_level += amount

    def __str__(self):
        '''возвращает строку, аккумулирующую состояние всех полей объекта'''
        pass

class Spell:
    def __init__(self):
        pass
