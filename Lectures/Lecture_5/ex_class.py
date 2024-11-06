class Dog:
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed

    def bark(self) -> None:
        print(f"{self.name} says \"BORK!\"")

    def get_name(self) -> str:
        return self.name
    
    def get_breed(self) -> str:
        return self.breed


if __name__=="__main__":
    lassie = Dog(name="Lassie", breed="Border Collie")
    print(lassie)
    lassie.bark()