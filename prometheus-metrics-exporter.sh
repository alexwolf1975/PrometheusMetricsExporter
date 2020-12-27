#!/bin/bash

eval $(python3 setenv.py)

until false
do
  mapfile metrics < <(wget --output-document=/dev/stdout --quiet http://$prometheus_host:$prometheus_port/metrics | grep ^[[:blank:]]*[^#] | sed "s/$/ $(date +%s)/")
  printf '%s' "${metrics[@]}" | nc -w$time_disconnect $graphite_host $graphite_port
  echo Got and sent ${#metrics[@]} metrics
  sleep $time_repeat
done
