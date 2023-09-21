def sum_digits(number):
    if not number.isdigit():
        print("Ошибка. ")
    else:
        number = int(number)
        if number > 0 :
            a = 0
            while number !=0:
                a += number
                number = number - 1
            print(a)
        else:
            print("Ошибка")

sum_digits(number = input("Введите число: "))