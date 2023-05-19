git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts" 2>nul || git -C "C:\zabscripts" pull || rmdir /S /Q "C:\zabscripts" && git clone "https://github.com/bag2000/zabscripts" "C:\zabscripts"
copy /Y "C:\zabscripts\UserParametrs.conf" "C:\Program Files\Zabbix Agent\zabbix_agentd.d\UserParametrs.conf"
net stop "Zabbix Agent"
timeout 60 > NUL
net start "Zabbix Agent"
