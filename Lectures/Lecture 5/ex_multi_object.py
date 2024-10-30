import ex_class


class Person:
    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age

    def pet(self, dog: ex_class.Dog) -> None:
        print(f"{self.name} is petting a {dog.get_breed()}")
        dog.bark()

if __name__=="__main__":
    john = Person(name="John", age=42.1)
    lassie = ex_class.Dog(name="Lassie", breed="Border Collie")
    john.pet(lassie)