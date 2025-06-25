# Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
# унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
# вычисления площади и периметра


import math

class Forma:
    def __init__(self,color,type):
        self.color = color
        self.type = type
class krug(Forma):
    def __init__(self, color, radius):
        super().__init__(color, 'Круг')
        self.radius = radius
    def ploshad(self):
            return math.pi * self.radius ** 2
    def perimetr(self):
            return 2 * math.pi * self.radius
krug = krug('Красный',5)
print(f"Цвет: {krug.color}, Тип: {krug.type}")
print(f"Площадь: {krug.ploshad()}")
print(f"Периметр: {krug.perimetr()}")


