#!/bin/sh
# Print dnsmasq stats
dnsmasqpid=$(ps aux | grep /usr/sbin/dnsmasq | grep -v grep | awk '{print $2}')
echo Sending USR1 to pid $dnsmasqpid
sudo kill -s USR1 $dnsmasqpid
sudo tail -7 /var/log/dnsmasq.log