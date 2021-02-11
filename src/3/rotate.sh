#!/bin/env bash
set -euo pipefail

function _d() {
        echo `date +%Y%m%d-`$1
}
if [ ! -d "/var/log/nginx" ]; then
    echo "nginx log folder doesnt exist, Exit"
fi
cd /var/log/nginx
h=$((`date +%H`-1))
if [ $h = -1 ]; then
        h=23
fi

d=`_d $h`
mv access.log access.log-$d
mv error.log error.log-$d
kill -USR1 `cat /var/run/nginx.pid`
sleep 1
gzip -f access.log-$d
gzip -f error.log-$d

# clean old
n=240
ls access.log-* -t | cut -d$'\n' -f $n- | xargs rm -f
ls error.log-* -t | cut -d$'\n' -f $n- | xargs rm -f