#1
class Animal:
    def __init__(self, name, type, age):
        self.name: str
        self.type: str
        self.age: int

    def make_sounds(self, sound: str):
        print(f"Animal {self.type} {self.name} make sounds '{sound}'")


example = Animal(name="Bobik", type="dog", age="5")
print(example)
example.make_sounds("gav-gav")


