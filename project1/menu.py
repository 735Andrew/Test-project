"""Библиотека, вычисляющая площади геометрических фигур"""

from figures import Circle, Triangle


def main():
    try:
        choice = int(
            input(
                "What figure`s area do you want to calculate ? \n"
                '("1" - Circle`s) ("2" - Triangle`s) ("3" - ?Mysterious?):  '
            )
        )
        if choice == 1:
            radius = int(input("Enter the circle`s radius: "))
            length = int(input("Enter the circle`s length: "))
            circle = Circle(
                radius=radius,
                length=length,
            )
            print(f"Circle`s area: {circle.calculate_area():.2f}")

        elif choice == 2:
            side_one = int(input("Enter the triangle`s first side: "))
            side_two = int(input("Enter the triangle`s second side: "))
            side_three = int(input("Enter the triangle`s third side: "))
            triangle = Triangle(
                side_one=side_one,
                side_two=side_two,
                side_three=side_three,
            )
            print(f"Triangle`s area: {triangle.calculate_area():.2f}")

        elif choice == 3:
            print(
                "Enter integer values for the desired variables.\n"
                'Use "-" to ignore a variable. Separate values with spaces.'
            )
            variables_string = input(
                "circumference length: length_one: length_two: length_three: "
            )
            print("Possible figures areas: ")

            variables = variables_string.split(" ")  # Сегрегация переменных
            clear_variables = [int(value) for value in variables if value != "-"]

            if len(clear_variables) >= 2:
                if int(variables[0]) == clear_variables[0]:
                    index = 1
                    while index < len(clear_variables):
                        circle = Circle(
                            radius=clear_variables[index],
                            length=clear_variables[0],
                        )
                        print(f"Circle`s area: {circle.calculate_area():.2f}")
                        index += 1

            if len(clear_variables) >= 4:
                triangle = Triangle(
                    side_one=clear_variables[1],
                    side_two=clear_variables[2],
                    side_three=clear_variables[3],
                )
                print(f"Triangle`s area: {triangle.calculate_area():.2f}")

            else:
                print("Enter more values")
        else:
            main()

    except ValueError as e:
        # Неправильный тип данных
        print(f"Error is: <{e}>")
        print("---")
        main()

    except KeyboardInterrupt:
        # Выход из программы
        pass


main()
