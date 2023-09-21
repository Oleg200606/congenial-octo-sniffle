def is_even(number):
    if not number.isdigit():
        print("Ошибка. ")
    else:
        number = int(number)
        if number % 2 == 0:
            print("True")
        else:
            print("False")




is_even(number = input("Введите число: "))