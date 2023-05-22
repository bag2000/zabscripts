"""
Модуль для работы с зависимостями
"""

import os
import sys
import printer


def pip_install(library):
    """
    Установка необходимого модуля. Необходимо наличие pip.exe
    (Windows - C:/Program Files/Python3/Scripts/pip.exe, Linux - /usr/bin/pip
    """

    if sys.platform == 'win32':
        path_to_pip = 'C:/Program Files/Python3/Scripts/pip.exe'
    else:
        path_to_pip = '/usr/bin/pip'

    if os.path.isfile(path_to_pip):
        printer.show_text(f'[!] "{path_to_pip}" => pip')
        if sys.platform == 'win32':
            stream = os.popen(f'\"sudo {path_to_pip}\" install %s' % library)
        else:
            stream = os.popen(f'sudo {path_to_pip} install {library}')
        result = stream.read()

        if 'Successfully installed' in str(result):
            printer.show_text('\n\n[+] Успешно установлено %s' % library)
            printer.show_text('[+] Повторите скрипт повторно')

        elif 'FAIL' in str(result).upper() or 'FAILED' in str(result).upper() \
                or 'FAILURE' in str(result).upper():
            printer.show_text('[!] Не удается установить модуль %d' % library)
            printer.show_text('[!] Запустите pip установку вручную на сервере')
            printer.show_text(f'[!] try: {path_to_pip} %s' % library)
            sys.exit()
    else:
        if sys.platform == 'win32':
            printer.show_text('Не найден файл C:/Program Files/Python3/Scripts/pip.exe')
        else:
            printer.show_text('Не найден файл /usr/bin/pip')
