'''ЗАДАНИЕ 1'''
"""
Написать скрипт, осуществляющий выборку определенных данных из файлов 
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import os
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


# Считывание txt-файлов и формирование списка кортежей с характеристиками ОС
# вынес в отдельную функцию
def read_data():
    data_dir = os.path.join(CURRENT_DIR, '../files\source_data')
    result = []
    # получаем список файлов директории source_data
    # и берем оттуда файлы с расширением txt
    data_txt_list = [el for el in os.listdir(data_dir) if el.split('.')[1] == 'txt']

    for file in data_txt_list:
        path_to_file = os.path.join(data_dir, file)

        with open(path_to_file) as f1:
            for line in f1.readlines():
                result += re.findall(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$', line)
    return result


# формируем список списков, кот. будут строками таблицы в csv файле
def get_data():
    # вызываем функцию read_data и сохраняем созданный ею список кортежей
    data = read_data()
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    # создаем списки, кот. будут строками таблицы
    # из каждого кортежа берем 2-й элемент, если имя 1-го элемента
    # совпадает с названиями столбцов в списке main_data
    for item in data:
        os_prod_list.append(item[1]) if item[0] == main_data[0][0] else None
        os_name_list.append(item[1]) if item[0] == main_data[0][1] else None
        os_code_list.append(item[1]) if item[0] == main_data[0][2] else None
        os_type_list.append(item[1]) if item[0] == main_data[0][3] else None

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


# создаем csv-файл
def write_to_csv(filepath):
    data = get_data()

    dir_, filename = os.path.split(filepath)

    os.makedirs(dir_, exist_ok=True)

    filepath = os.path.join(CURRENT_DIR, dir_, filename)

    with open(filepath, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        for line in data:
            writer.writerow(line)


if __name__ == '__main__':
    write_to_csv('../files\source_data/os_data_report.csv')
