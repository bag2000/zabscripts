net stop "Zabbix Agent"
timeout 60 > NUL
net start "Zabbix Agent"
