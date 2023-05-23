"""
Модуль для работы с выводом сообщений на экран
"""

import sys


def show_text(text, end: bool = True):
    """
    Метод кодирует текст в utf8 и выводит текст на экран
    :param text: Текст для вывода на экран
    :param end: Добовлять перенос строки или нет. True - да, False - нет.
    """
    if end:
        text = str(text) + '\n'
    else:
        text = str(text)
    text = text.encode('utf-8')
    sys.stdout.buffer.write(text)
