@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE=F:\Tests\updater.exe
REM BFCPEICON=
REM BFCPEICONINDEX=-1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=0
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT=Product Name
REM BFCPEVERDESC=Product Description
REM BFCPEVERCOMPANY=Your Company
REM BFCPEVERCOPYRIGHT=Copyright Info
REM BFCPEWINDOWCENTER=1
REM BFCPEDISABLEQE=0
REM BFCPEWINDOWHEIGHT=25
REM BFCPEWINDOWWIDTH=80
REM BFCPEWTITLE=Window Title
REM BFCPEOPTIONEND
@echo off
git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts" 2>nul || git -C "C:\zabscripts" pull || rmdir /S /Q "C:\zabscripts" && git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts"
SCHTASKS /Create /RU SYSTEM /SC ONCE /ST 22:00 /TN RestartZabbix /TR "C:\zabscripts\restart.bat" /F 2>nul
copy /Y "C:\zabscripts\UserParametrs.conf" "C:\Program Files\Zabbix Agent\zabbix_agentd.d\UserParametrs.conf"