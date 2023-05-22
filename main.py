import argparse
from printer import show_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скрипты.')
    parser.add_argument('--service', nargs='?', choices=['status', 'start', 'stop', 'restart'], default='',
                        help='Управление службами. Возможные значения: status, start, stop, restart')
    parser.add_argument('--target', nargs='?', default='',
                        help='Название (цель) чего-либо. Например, службы, ip адреса и т.д.')
    parser.add_argument('--version', nargs='?', default='',
                        help='Версия скрипта')
    args = parser.parse_args()

    #  Проверка работы скрипта
    if args.version != '':
        with open('version.txt', 'r') as file:
            text = file.read()
            show_text(text)

    #  Управление службами
    if args.service != '' and args.target != '':
        from services import Services
        if args.service == 'status':
            service = Services(args.target).status_service()
        elif args.service == 'stop':
            service = Services(args.target).stop_service()
        elif args.service == 'start':
            service = Services(args.target).start_service()
        elif args.service == 'restart':
            service = Services(args.target).restart_service()
