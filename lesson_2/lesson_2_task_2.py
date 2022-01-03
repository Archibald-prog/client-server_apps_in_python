'''ЗАДАНИЕ 2'''
"""Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, 
автоматизирующий его заполнение данными. Для этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра."""

import json
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def write_order_to_json(item, quantity, price, buyer, date):
    filepath = os.path.join(CURRENT_DIR, '../files', 'orders.json')
    to_json = {}

    with open(filepath, encoding='utf-8') as f1:
        to_json = json.loads(f1.read())
        data_dict = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }

    to_json['orders'].append(data_dict)

    with open(filepath, 'w', encoding='utf-8') as f1:
        json.dump(to_json, f1, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    write_order_to_json('Занимательная арифметика', '1', '100', 'Семен Фактура', '22.12.2021')
    write_order_to_json('Грокаем алгоритмы', '5', '300', 'Василий Пупкин', '15.11.2021')
