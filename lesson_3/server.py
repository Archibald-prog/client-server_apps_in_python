import json
import sys
import socket

from utils import load_configs, get_message, send_message

CONFIGS = dict()


def handle_message(message, CONFIGS):
    if CONFIGS.get('ACTION') in message \
            and message[CONFIGS.get('ACTION')] == CONFIGS.get('PRESENCE') \
            and CONFIGS.get('TIME') in message \
            and CONFIGS.get('USER') in message \
            and message[CONFIGS.get('USER')][CONFIGS.get('ACCOUNT_NAME')] == 'Guest':
        return {CONFIGS.get('RESPONSE'): 200}
    return {
        CONFIGS.get('RESPONSE'): 400,
        CONFIGS.get('ERROR'): 'Bad Request'
    }


def main():
    global CONFIGS
    # вызываем функцию load_configs() из модуля utils.py
    # с параметром по умолчанию is_server=True
    CONFIGS = load_configs()
    try:
        # если при запуске скрипта передается флаг -p, то после него
        # в списке параметров sys.argv доолжен быть указан порт для прослушивания
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            # если флага -р нет - слушаем порт по умолчанию
            listen_port = CONFIGS.get('DEFAULT_PORT')
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        print('После -\'p\' необходимо указать порт')
        sys.exit(1)
    except ValueError:
        print(
            'Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    try:
        # если при запуске скрипта передается флаг -а, то после него
        # в списке параметров sys.argv доолжен быть указан IP-адрес для прослушивания
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
            # если флага -а нет - слушаем все доступные адреса
        else:
            listen_address = ''

    except IndexError:
        print(
            'После \'a\'- необходимо указать адрес для ')
        sys.exit(1)
    # создаем сокет TCP
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # приявязыаем сокет к IP-адресу и порту клиента
    transport.bind((listen_address, listen_port))
    # максимальное число одновременных запросов берем из config.json
    transport.listen(CONFIGS.get('MAX_CONNECTIONS'))

    while True:
        client, client_address = transport.accept()
        try:
            # в функцию get_message() передаем конфигурации,
            # которые возвращает функция load_configs() из модуля utils.py
            message = get_message(client, CONFIGS)
            response = handle_message(message, CONFIGS)
            send_message(client, response, CONFIGS)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
