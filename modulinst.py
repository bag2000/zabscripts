import os
import sys
import printer


def pip_install(library):
    """Locate pip.exe on system and install library.
    Be sure to sanitize input to prevent RCE."""

    if sys.platform == 'win32':
        path_to_pip = 'C:/Program Files/Python3/Scripts/pip.exe'
    else:
        path_to_pip = '/usr/bin/pip'

    if os.path.isfile(path_to_pip):
        printer.show_text(f'[!] "{path_to_pip}" => pip')
        stream = os.popen(f'\"{path_to_pip}\" install %s' % library)
        result = stream.read()

        if 'Successfully installed' in str(result):
            printer.show_text('\n\n[+] Successfully installed %s' % library)
            printer.show_text('Please try again!')
            sys.exit()

        elif 'FAIL' in str(result).upper() or 'FAILED' in str(result).upper() \
                or 'FAILURE' in str(result).upper():
            printer.show_text('[!] Unable to install %d' % library)
            printer.show_text('[!] Please manually run the pip installer')
            printer.show_text(f'[!] try: {path_to_pip} %s' % library)
            sys.exit()
