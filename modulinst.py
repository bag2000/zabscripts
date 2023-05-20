import os
import sys
import printer


def pip_install(library):
    """Locate pip.exe on system and install library.
    Be sure to sanitize input to prevent RCE."""

    if os.path.isfile("C:/Program Files/Python3/Scripts/pip.exe"):
        printer.show_text('[!] "C:/Program Files/Python3/Scripts/pip.exe" => pip')
        stream = os.popen('\"C:/Program Files/Python3/Scripts/pip.exe\" install %s' % library)
        result = stream.read()

        if 'Successfully installed' in str(result):
            printer.show_text('\n\n[+] Successfully installed %s' % library)
            printer.show_text('Please try again!')
            sys.exit()

        elif 'FAIL' in str(result).upper() or 'FAILED' in str(result).upper() \
                or 'FAILURE' in str(result).upper():
            printer.show_text('[!] Unable to install %d' % library)
            printer.show_text('[!] Please manually run the pip installer')
            printer.show_text('[!] try: C:/Program Files/Python3/Scripts/pip.exe %s' % library)
            sys.exit()
