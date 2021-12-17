"""ЗАДАНИЕ 3"""
'''
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
'''
str_list = ['attribute', 'класс', 'функция', 'type']
not_ascii_list = [el for el in str_list if not el.isascii()]
print(f"the strings you can't write in byte type - {', '.join(not_ascii_list)}")
