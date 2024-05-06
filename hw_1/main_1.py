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
