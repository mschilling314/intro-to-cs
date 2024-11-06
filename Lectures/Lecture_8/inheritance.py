class Shape:
    def __init__(self) -> None:
        pass

    def perimeter(self) -> float:
        pass

    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def perimeter(self) -> float:
        return 2*(self.width + self.height)
    
    def area(self) -> float:
        return self.width * self.height