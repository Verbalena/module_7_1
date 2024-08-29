# Задача "Учёт товаров"
import os
from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop():
    __file_name = 'products.txt'  # Инкапсулированный атрибут

    def get_products(self):       # cчитывет всю информацию из файла
        with open(self.__file_name, 'r', encoding='utf-8') as file:  # открыть файл в режиме чтения и потом закрыть
            file_content = file.read()    # прочитать файл
            return str(file_content)  # вернуть строку из файла

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')       # открыть файл в режиме добавления
        for product in products:
            if str(product.name) not in current_products:    # проверить присутствует ли строка в файле
                file.write(str(product) + '\n')           # добавить строку в файл
                current_products += str(product) + '\n'
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__

s1.add(p1, p2, p3)       
print(s1.get_products())
