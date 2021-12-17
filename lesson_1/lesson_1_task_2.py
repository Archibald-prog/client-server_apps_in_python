"""ЗАДАЧА 2"""
"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""

bytes_str_1 = b'class'
bytes_str_2 = b'function'
bytes_str_3 = b'method'

print(f'bytes_str_1 content - {bytes_str_1}')
print(f'bytes_str_1 type - {type(bytes_str_1)}')
print(f'bytes_str_1 length - {len(bytes_str_1)} bits')
print('=============================================')

print(f'bytes_str_2 content - {bytes_str_2}')
print(f'bytes_str_2 type - {type(bytes_str_2)}')
print(f'bytes_str_2 length - {len(bytes_str_2)} bits')
print('=============================================')

print(f'bytes_str_3 content - {bytes_str_3}')
print(f'bytes_str_3 type - {type(bytes_str_3)}')
print(f'bytes_str_3 length - {len(bytes_str_3)} bits')
print('=============================================')
