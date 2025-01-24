# Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.
while True:
    try:
        s = input("Введите строку = ")
        i = 1 
        otvet = 0
        for i in s:
            n = int(ord(i))
            if 97 <= n <= 122:
                otvet += 1
        print(f'кол-во латинских прописных букв в этой строке = {otvet}')
        break        

    except ValueError:
        print("Ошибка, Введите строку")
