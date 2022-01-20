"""ЗАДАЧА 5"""
'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
'''

import subprocess

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    # декодируем вывод модуля subprocess в строку
    # используем кодировку cp866, т.к. исходный байтовый формат - cp866
    # затем кодирем строку в байты с кодировкой utf-8
    line = line.decode('cp866').encode('utf-8')
    # преобразуем вывод снова в строковый тип с с кодировкой utf-8
    print(line.decode('utf-8'))
print('==========================================================')

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
print('==========================================================')
