"""ЗАДАЧА 1"""
"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

string_1 = 'разработка'
string_2 = 'сокет'
string_3 = 'декоратор'

print(f'string_1 content - {string_1}')
print(f'string_1 type - {type(string_1)}')
print('=================================')

print(f'string_2 content - {string_2}')
print(f'string_2 type - {type(string_2)}')
print('=================================')

print(f'string_3 content - {string_3}')
print(f'string_3 type - {type(string_3)}')
print('=================================')

# коневертируем с использованием utf-16
string_1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
string_2_unicode = '\u0441\u043e\u043a\u0435\u0442'
string_3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(f'string_1_unicode content - {string_1_unicode}')
print(f'string_1_unicode type - {type(string_1_unicode)}')
print('=================================')

print(f'string_2_unicode content - {string_2_unicode}')
print(f'string_2_unicode type - {type(string_2_unicode)}')
print('=================================')

print(f'string_3_unicode content - {string_3_unicode}')
print(f'string_3_unicode type - {type(string_3_unicode)}')
print('=================================')