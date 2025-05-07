import pytest
from figures import Circle, Triangle


@pytest.fixture
def circle():
    return Circle(radius=5, length=15)


def test_circle_area_first(circle):
    assert int(circle.calculate_area()) == 314


def test_circle_area_second(circle):
    with pytest.raises(Exception):
        assert circle.calculate_area() == 100


@pytest.mark.parametrize("test_input, expected", [("3 4 5", 6), ("7 14 0", None)])
def test_triangle_area(test_input, expected):

    values = test_input.split(" ")
    values = list(map(lambda value: int(value), values))

    side_one, side_two, side_three = values
    triangle = Triangle(side_one, side_two, side_three)
    assert triangle.calculate_area() == expected


def test_triangle_is_rectangular():
    t = Triangle(side_one=3, side_two=5, side_three=4)
    assert t.is_rectangular() is True
