import os
import sys
from printer import show_text as show
from modulinst import pip_install as pipi
import time

try:
    import psutil
except Exception as e:
    show('[!] Error importing psutil ... Trying pip installer')
    pipi('psutil')
    with open('log.log', 'w') as file:
        file.write(str(e))


class Services:

    def __init__(self, name_service: str):
        self.name_service = name_service
        self.service = psutil.win_service_get(self.name_service)

    def status_service(self):
        show(f'Статус службы {self.name_service} - {self.service.status()}')

    def stop_service(self):

        if self.service.status() != 'stopped':
            seconds = 30
            os.popen(f"net stop {self.name_service} 1>nul 2>nul")
            while self.service.status() != 'stopped':
                time.sleep(1)
                seconds -= 1
                show(f'Служба {self.name_service} останавливается.')
                if seconds <= 0:
                    show(f'Не удалось остановить службу {self.name_service}')
                    sys.exit()
            show(f'Служба {self.name_service} оастановлена.')
        else:
            show(f'Служба {self.name_service} не запущена.')

    def start_service(self):

        if self.service.status() != 'running':
            seconds = 30
            os.popen(f"net start {self.name_service} 1>nul 2>nul")
            while self.service.status() != 'running':
                time.sleep(1)
                seconds -= 1
                show(f'Служба {self.name_service} запускается.')
                if seconds <= 0:
                    show(f'Не удалось запустить службу {self.name_service}')
                    sys.exit()
            show(f'Служба {self.name_service} запущена.')
        else:
            show(f'Служба {self.name_service} запущена.')

    def restart_service(self):

        self.stop_service()
        self.start_service()