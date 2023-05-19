#!/bin/bash

cat << EOF > /usr/bin/RestartZabbix.sh
#!/bin/bash
git clone "https://github.com/bag2000/zabscripts" "/zabscripts" 2>/dev/null || \
git -C "/zabscripts" pull 2>/dev/null || rm -r "/zabscripts" 2>/dev/null && \
git clone "https://github.com/bag2000/zabscripts" "/zabscripts" 2>/dev/null
cp /zabscripts/UserParametrs-linux.conf /etc/zabbix/zabbix_agentd.d/UserParametrs-linux.conf
systemctl restart zabbix-agent
systemctl stop RestartZabbix.service
EOF
cp /zabscripts/UserParametrs-linux.conf /etc/zabbix/zabbix_agentd.d/UserParametrs-linux.conf
systemctl restart zabbix-agent
chmod +x /usr/bin/RestartZabbix.sh

cat << EOF > /lib/systemd/system/RestartZabbix.service

[Unit]
Description=My Shell Script

[Service]
ExecStart=/usr/bin/RestartZabbix.sh

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload
