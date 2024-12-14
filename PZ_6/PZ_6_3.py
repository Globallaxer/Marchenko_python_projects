# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).
import random 

while True:
    try:
        a = []
        n = int(input("Введите размер списка:  "))
        i = 1
        while i <= n:
            b = random.randint(0, 10)
            a.append(b)
            i += 1
        print(f'Созданный список: {a}')
        last_fragment = a[-1]
        for d in range(len(a) -1, 0 , -1) :
            a[d] = a[d + 1]
        a[0] = last_fragment

        print(f"Список после циклического сдвига - {a}")               
            
        break

    except ValueError:
        print("Ошибка, введите число")
