'''ЗАДАНИЕ 3'''
"""Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными."""

import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(CURRENT_DIR, '../files', 'file.yaml')
data = {
    'items': ['table', 'chair', 'sofa', 'computer desk'],
    'quantity': 4,
    'price': {
        'table': '100€',
        'chair': '5€',
        'sofa': '400€',
        'computer desk': '150€'
    }
}

with open(filepath, 'w') as f1:
    yaml.dump(data, f1, default_flow_style=False, allow_unicode=True)

with open(filepath) as f1:
    print(f1.read())
