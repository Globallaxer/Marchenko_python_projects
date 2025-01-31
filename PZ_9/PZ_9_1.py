# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {'BMW':['XM', 'X7', 'X6 M'],'Shevrolet':['Apache','Astra','Aveo'],'lada':['Granta Седан','Granta лифтбек','Granta Cross'] }
print(f'2 модель BMW = {avto['BMW'][1]}, 2 модель Shevrolet = {avto["Shevrolet"][1]},2 модель lada = {avto["lada"][1]}, все модели = {avto["BMW"][0:3]},{avto.get('Shevrolet')},{avto["lada"][:]}')

