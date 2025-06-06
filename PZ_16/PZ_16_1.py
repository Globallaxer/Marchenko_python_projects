# . Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
# Напишите метод, который выводит информацию о машине в формате "Марка:
# марка, Модель: модель, Год выпуска: год".

class car :
    def __init__(self,marl,model,year):
        self.marl=marl
        self.model=model
        self.year=year
    def vsvod(self):
        print(f'Марка:{self.marl},Модель={self.model},Год выпуска = {self.year}')
car1 = car("BMW","X5","2015")     
car1.vsvod   