# . Составить генератор (yield), который выводит из строки только цифры.
def extract_digits(s):
    for char in stroka:
        if char.isdigit():
            yield char
stroka = input('')
digits = extract_digits(stroka)
# for digit in digits:
#     print(digit)
otvet = [digit for digit in digits]
print(otvet)