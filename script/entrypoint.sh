#!/bin/sh
echo "=======LOAD MODULE========"
echo $DJANGO_SETTINGS_MODULE
echo "=========================="
doit prepare
touch /var/run/supervisor.sock && chmod 777 /var/run/supervisor.sock
supervisord -c /app/proc/supervisor.conf -n