# Программа должна обеспечивать функционал по вводу данных в БД (10 позиций), их
#поиску(SELECT), удалению(DELETE) и редактированию(UPDATE). При организации поиска, удаления и
#редактирования использовать WHERE, предусмотреть по три SQL-запроса для каждой
#операции


# Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
import sqlite3
from datetime import datetime


conn = sqlite3.connect('trade_company.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date TEXT,
    product TEXT,
    amount REAL,
    discount REAL,
    branch TEXT,
    manager TEXT
)
''')
conn.commit()


def add_sale(sale_date, product, amount, discount, branch, manager):
    cursor.execute('''
    INSERT INTO sales (sale_date, product, amount, discount, branch, manager)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (sale_date, product, amount, discount, branch, manager))
    conn.commit()


sales_data = [
    ('2025-06-01', 'Телевизор', 30000, 5, 'Москва', 'Иванов'),
    ('2025-06-02', 'Холодильник', 25000, 10, 'Санкт-Петербург', 'Петров'),
    ('2025-06-03', 'Микроволновка', 7000, 0, 'Москва', 'Иванов'),
    ('2025-06-04', 'Пылесос', 12000, 7, 'Новосибирск', 'Сидоров'),
    ('2025-06-05', 'Стиральная машина', 28000, 15, 'Москва', 'Иванов'),
    ('2025-06-06', 'Кондиционер', 22000, 5, 'Санкт-Петербург', 'Петров'),
    ('2025-06-07', 'Утюг', 1500, 0, 'Новосибирск', 'Сидоров'),
    ('2025-06-08', 'Телефон', 15000, 12, 'Москва', 'Иванов'),
    ('2025-06-09', 'Ноутбук', 45000, 10, 'Санкт-Петербург', 'Петров'),
    ('2025-06-10', 'Планшет', 20000, 8, 'Новосибирск', 'Сидоров'),
]

for sale in sales_data:
    add_sale(*sale)



def search_product(product_name):
    cursor.execute('SELECT * FROM sales WHERE product = ?', (product_name,))
    return cursor.fetchall()

def search_branch(branch_name):
    cursor.execute('SELECT * FROM sales WHERE branch = ?', (branch_name,))
    return cursor.fetchall()

def search_managerdiscount(manager_name, min_discount):
    cursor.execute('SELECT * FROM sales WHERE manager = ? AND discount >= ?', (manager_name, min_discount))
    return cursor.fetchall()



def delete_product(product_name):
    cursor.execute('DELETE FROM sales WHERE product = ?', (product_name,))
    conn.commit()

def delete_branch(branch_name):
    cursor.execute('DELETE FROM sales WHERE branch = ?', (branch_name,))
    conn.commit()

def delete_mandate(manager_name, sale_date):
    cursor.execute('DELETE FROM sales WHERE manager = ? AND sale_date = ?', (manager_name, sale_date))
    conn.commit()



def update_product(product_name, new_discount):
    cursor.execute('UPDATE sales SET discount = ? WHERE product = ?', (new_discount, product_name))
    conn.commit()

def update_branch(branch_name, new_amount):
    cursor.execute('UPDATE sales SET amount = ? WHERE branch = ?', (new_amount, branch_name))
    conn.commit()

def update_man_date(sale_date, product_name, new_manager):
    cursor.execute('UPDATE sales SET manager = ? WHERE sale_date = ? AND product = ?', (new_manager, sale_date, product_name))
    conn.commit()



# print("Поиск по продукту 'Телевизор':")
# print(search_product('Телевизор'))

# print("\nПоиск по филиалу 'Москва':")
# print(search_branch('Москва'))

# print("\nПоиск по менеджеру 'Иванов' с минимальной скидкой 5%:")
# print(search_managerdiscount('Иванов', 5))

# print("\nОбновление скидки для 'Телевизор' до 10%")
# update_product('Телевизор', 10)
# print(search_product('Телевизор'))

# print("\nУдаление записей по филиалу 'Новосибирск'")
# delete_branch('Новосибирск')
# print("Все записи после удаления филиала Новосибирск:")



conn.close()