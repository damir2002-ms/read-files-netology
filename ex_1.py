import os

def parse_ingredient(line):
    """
    Парсит строку с ингредиентом и возвращает словарь с его характеристиками.
    """
    name, quantity, measure = map(str.strip, line.split('|'))
    return {'ingredient_name': name, 'quantity': int(quantity), 'measure': measure}

def read_recipes(file_path):
    """
    Читает рецепты из файла и возвращает словарь с кулинарной книгой.
    """
    cook_book = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = [parse_ingredient(file.readline().strip()) for _ in range(ingredient_count)]
            cook_book[dish_name] = ingredients
    
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Возвращает словарь с ингредиентами и их количеством для указанных блюд и количества персон.
    """
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list

# Путь к файлу с рецептами
file_path = r'D:\рс\python\NETOLOGY\cook_book\recipes.txt'

# Чтение рецептов из файла
cook_book = read_recipes(file_path)

# Пример вызова функции
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

# Получение списка покупок
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)
