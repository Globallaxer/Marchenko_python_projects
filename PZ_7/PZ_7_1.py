# Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.
while True:
    try:
        s = input()
        i = 1 
        b = 0
        sl = s.join
        print(len(sl))
        for i in range(len(s)):
            if i == 'a'   :
              b += 1
        print(b)
        break     
        break 
    except ValueError:
        print("a")

               