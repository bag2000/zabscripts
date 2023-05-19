SCHTASKS /Create /RU SYSTEM /SC ONCE /ST 22:00 /TN RestartZabbix /TR "C:\zabscripts\restart.bat" /F
SCHTASKS /Run /I /TN RestartZabbix
