# С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа. Заключить слово в рамку из полученных линий.
while True:
    try:
        name = str(input("Введите строку: "))
        def horizont_line(horizont):
            print('-' * horizont)
        def draw_name(word):
            horizont = len(name) + 2
            horizont_line(horizont)
            print("|" + word + "|")  
            horizont_line(horizont)
        draw_name(name)
        break       

    except ValueError:
        print('Ошибка, введите строку')