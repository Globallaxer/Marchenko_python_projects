#1. Дано целое число. Если оно является положительным, то прибавить к нему 1; если
# отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Вывести полученное число.
while True:

    a = input("Введите целое число ")
    try:
        number_a = int(a)
        if number_a == 0:
            number_a = 10
            print(number_a)
            break
        elif number_a < 0:
            number_a -= 2
            print(number_a)
            break
        elif number_a > 0:
            number_a += 1
            print(number_a)
            break
    except ValueError:
        print("Ошибка, введите целое число")

