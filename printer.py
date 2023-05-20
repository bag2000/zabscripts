import sys


def show_text(text):
    text = str(text) + '\n'
    text = text.encode('utf8')
    sys.stdout.buffer.write(text)
