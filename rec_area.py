def rectangle_area(width, height):
    if not width.isdigit() or not height.isdigit():
        print("Ошибка. ")
    else:
        width = float(width)
        height = float(height)
        if width <= 0 or height <= 0:
            print("Ошибка: введите числа больше нуля")
        else:
            return width * height

width_input = input("Введите длину первой стороны прямоугольника: ")
height_input = input("Введите длину второй стороны прямоугольника: ")

result = rectangle_area(width_input, height_input)
if result is not None:
    print("Площадь прямоугольника:", result)
