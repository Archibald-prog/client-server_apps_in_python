import json
import os
import sys


def load_configs(is_server=True):
    config_keys = [
        'DEFAULT_PORT',
        'MAX_CONNECTIONS',
        'MAX_PACKAGE_LENGTH',
        'ENCODING',
        'ACTION',
        'TIME',
        'USER',
        'ACCOUNT_NAME',
        'PRESENCE',
        'RESPONSE',
        'ERROR'
    ]
    # если функцию вызвает клиент - добавляем в список ключей дефолтный IP
    if not is_server:
        config_keys.append('DEFAULT_IP_ADDRESS')
    if not os.path.exists('config.json'):
        print('Файл конфигурации не найден')
        sys.exit(1)
    with open('config.json') as config_file:
        # получаем содержимое файла config.json в виде словаря Python
        CONFIGS = json.load(config_file)
        # получаем список ключей из файла config.json
    loaded_configs_keys = list(CONFIGS.keys())
    # сравниваем списки loaded_config_keys и config_keys
    # сообщаем, если в config.json не хватает какого-то ключа
    for key in config_keys:
        if key not in loaded_configs_keys:
            print(f'В файле конфигурации не хватает ключа: {key}')
            sys.exit(1)
    return CONFIGS  # возвращает словарь с конфигурациями


def send_message(opened_socket, message, CONFIGS):
    # из словаря Python получаем строку в формате json
    # кодируем строку, взяв кодировку из файла конфигураций
    json_message = json.dumps(message)
    response = json_message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(response)


def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(CONFIGS.get('MAX_PACKAGE_LENGTH'))
    # проверяем: если сообщение пришло в байтах,
    # его нужно декодировать, взяв кодировку из файла конфигураций
    # если нет - выбросить ошибку
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGS.get('ENCODING'))
        # получаем словарь Python
        response_dict = json.loads(json_response)
        # проверка: действительно ли сообщение преобразовано в словарь Python
        # если да - вернуть словарь, в прот. случае выбросить ошибку
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError
