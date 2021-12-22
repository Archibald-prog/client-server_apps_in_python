"""ЗАДАЧА 6"""
"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

with open(r"../files\test_file.txt", "w") as f1:
    f1.write('сетевое программирование сокет декоратор')
f1 = open(r"../files\test_file.txt")
print(f1.read())  # --> сетевое программирование сокет декоратор

# узнаем кодировку файла по умолчанию
print(locale.getpreferredencoding())  # --> cp1251
# узнаем реальную кодировку файла - в параметре encoding
print(f1)  # --> <_io.TextIOWrapper name='files\\test_file.txt' mode='r' encoding='cp1251'>
print('=================================================================================')

'''
Если попытаться открыть файл с кодировкой utf-8, код падает с ошибкой:
with open(r'../files\test_file.txt', encoding='utf-8') as f1:
    print(f1.read())
Поэтому надо сначала закодировать строку в utf-8, 
а потом раскодировать с этой же кодировкой: 
'''
with open(r"../files\test_file.txt") as f1:
    # кодируем файл в utf-8
    unicode_bytes = f1.read().encode('utf-8')
    print(unicode_bytes)
    # декодируем в utf-8
    unicode_str = unicode_bytes.decode('utf-8')
    print(unicode_str)  # --> сетевое программирование сокет декоратор
print('=================================================================================')

'''
Другой вариант - изначально создать файл в кодировке utf-8, а потом открыть его на чтение 
с этой же кодировкой. 
'''
with open(r"../files\test_file_2.txt", "w", encoding='utf-8') as f1:
    f1.write('нечто совершенно иное')
f1 = open(r"../files\test_file_2.txt", encoding='utf-8')
unicode_str = f1.read()
print(unicode_str)
# кодировка по умолчанию - по-прежнему cp1251,
# но реальная кодировка изменилась на utf-8
print(locale.getpreferredencoding())
print(f1)


