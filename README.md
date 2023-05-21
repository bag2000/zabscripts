
SCHTASKS /Run

Zabbix  
	Если Windows:  
		Устанавливаем Python  
			1. Запускаем установщик под админом  
			2. При установке ставим галочку Add python.exe to PATH  
			3. Выбираем Customize installation  
			4. Optional Features - Все галочки  
			5. Advanced Options  
			5.1 Ставим галочку Install Python for all users  
			5.2 Снимаем галочку с Create shotcuts for installed applications  
			5.3 Путь установки - C:\Program Files\Python3  
		Устанавливаем Git  
		Настраиванм Timeout 30 Zabbix Agent  

	Если Linux:  
		apt install - y git
		apt-get install -y python3-pip
		python3 -m pip install gitpython
		mkdir -m 777 /zabscripts
		chown -R zabbix /zabscripts
		
		Копируем файлы из папка zabscripts в созданую папку zabscripts
		
		Далее
		cp /zabscripts/UserParametrs-linux.conf /etc/zabbix/zabbix_agentd.d/
		chown zabbix /etc/zabbix/zabbix_agentd.d/UserParametrs-linux.conf
		systemctl restart zabbix-agent
	