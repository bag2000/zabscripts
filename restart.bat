git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts" 2>nul || git -C "C:\zabscripts" pull || rmdir /S /Q "C:\zabscripts" && git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts"
net stop "Zabbix Agent"
timeout 10 > NUL
net start "Zabbix Agent"
