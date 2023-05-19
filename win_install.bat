SCHTASKS /Create /RU SYSTEM /SC ONCE /ST 22:00 /TN RestartZabbix /TR "C:\zabscripts\restart.bat" /F
curl -L https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe -o "C:\zabscripts\python.exe"
"C:\zabscripts\python.exe" /quiet Include_debug=0 Include_symbols=0 Shortcuts=0 AssociateFiles=1 Include_launcher=0 Include_tcltk=0 InstallAllUsers=1 PrependPath=1 TargetDir="C:\Program Files\Python3"
del /Q "C:\zabscripts\python.exe"
curl -L https://github.com/git-for-windows/git/releases/download/v2.41.0-rc0.windows.1/Git-2.41.0-rc0-64-bit.exe -o "C:\zabscripts\git.exe"
"C:\zabscripts\git.exe" /VERYSILENT /NORESTART
del /Q "C:\zabscripts\git.exe"
SCHTASKS /Run /I /TN RestartZabbix
