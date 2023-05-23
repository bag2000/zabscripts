import argparse
from printer import show_text

version = '1.2.0'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скрипты.')
    parser.add_argument('--kick', nargs='?', default='',
                        help='Название учетной записи которую необходимо кикнуть')
    parser.add_argument('--reboot', action='store_const', const=version, help='Перезагрузка сервера')
    parser.add_argument('--service', nargs='?', choices=['status', 'start', 'stop', 'restart'], default='',
                        help='Управление службами. Возможные значения: status, start, stop, restart\n'
                             'Используется совместно с --target\n'
                             'Пример: python main.py --service status --target MSSQLSERVER')
    parser.add_argument('--target', nargs='?', default='',
                        help='Название (цель) чего-либо. Например, службы, ip адреса и т.д.')
    parser.add_argument('--version', action='store_const', const=version, help='Вывод версии скрипта')
    args = parser.parse_args()

    # Вывод врсии скрипта
    if args.version is not None:
        show_text(args.version, end=False)

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

    # Перезагрузка сервера
    if args.reboot is not None:
        import sys
        import os
        if sys.platform == 'win32':
            os.popen('shutdown -g -f -t 0')
            show_text('Передан сигнал перезагрузки')
        else:
            os.popen('reboot')
            show_text('Передан сигнал перезагрузки')

    # Кикнуть пользователя
    if args.kick != '':
        import os
        session = os.popen(f'qwinsta | findstr {args.kick}').read()[1:].split()[0]
        kick = os.popen(f'rwinsta {session} /server:localhost')
