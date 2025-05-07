import math


class Figure:
    """Класс, характеризующий любые геометрические фигуры"""

    def __init__(self, *args, **kwargs):
        pass

    def calculate_area(self) -> int:
        pass


class Circle(Figure):
    """Класс, характеризующий фигуру круг"""

    def __init__(self, radius, length, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius
        self.length = length
        self.diameter = radius * 2
        self.pi = math.pi

    def calculate_area(self) -> int | None:
        if self.radius >= 1 and self.diameter >= 1:  # Проверка значений
            return self.pi * (self.diameter**2)
        else:
            return None


class Triangle(Figure):
    """Класс, характеризующий фигуру треугольник"""

    def __init__(self, side_one, side_two, side_three, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.perimeter = side_one + side_two + side_three
        self.semi_perimeter = self.perimeter / 2

    def calculate_area(self) -> int | None:
        if (
            # Проверка значений
            self.semi_perimeter >= 1
            and self.side_one >= 1
            and self.side_two >= 1
            and self.side_three >= 1
        ):
            return (
                self.semi_perimeter
                * (self.semi_perimeter - self.side_one)
                * (self.semi_perimeter - self.side_two)
                * (self.semi_perimeter - self.side_three)
            ) ** 0.5
        else:
            return None

    def is_rectangular(self):
        sides = [self.side_one, self.side_two, self.side_three]
        greatest_side = max(sides)
        side_two, side_three = [side for side in sides if side != greatest_side]
        return greatest_side**2 == (side_two**2 + side_three**2)