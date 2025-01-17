# Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке гласных букв.
while True:
    try:
        s = input("Введите строку = ")
        i = 1 
        otvet = 0
        for i in s:
            n = int(ord(i))
            if n == 1072 or 1092 or 1080 or 1103 or 1105 or 1077 or 1086 or 1101 or 1099:
                otvet += 1
        print(f'кол-во русских гласных букв в этой строке = {otvet}')
        break        

    except ValueError:
        print("Ошибка, Введите строку")