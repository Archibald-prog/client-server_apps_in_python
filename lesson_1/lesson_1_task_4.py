"""ЗАДАЧА 4"""

'''
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
'''

str_list = ['разработка', 'администрирование', 'protocol', 'standard']
bytes_list = [el.encode('utf-16') for el in str_list]
reverse_decoding_list = [el.decode('utf-16') for el in bytes_list]
print(f"Initial list - {', '.join(str_list)}")
print(*bytes_list, sep="\n")
print(f"Final list - {', '.join(reverse_decoding_list)}")