from services import Services
import sys
from printer import show_text as show
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Скрипты.')
    parser.add_argument('--service', nargs='?', choices=['status', 'start', 'stop', 'restart'], default='',
                        help='Управление службами. Возможные значения: status, start, stop, restart')
    parser.add_argument('--target', nargs='?', default='',
                        help='Название (цель) чего-либо. Например, службы, ip адреса и т.д.')
    args = parser.parse_args()

    if args.service != '' and args.target != '':
        if args.service == 'status':
            service = Services(args.target).status_service()
        elif args.service == 'stop':
            service = Services(args.target).stop_service()
        elif args.service == 'start':
            service = Services(args.target).start_service()
        elif args.service == 'restart':
            service = Services(args.target).restart_service()
