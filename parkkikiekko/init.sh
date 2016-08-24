#! /bin/sh

SERVICE=parkkikiekko.sh

### BEGIN INIT INFO
# Provides:          parkkikiekko
# Required-Start:    $remote_fs $syslog $time
# Required-Stop:     $remote_fs $syslog $time
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Simple script to start a program at boot
# Description:       Parkkikiekko
### END INIT INFO

case "$1" in
  start)
    echo "Starting $SERVICE"
    /home/pi/work/ZeroSeg/parkkikiekko/$SERVICE &
    ;;
  stop)
    echo "Stopping $SERVICE"
    killall $SERVICE
    ;;
  *)
    echo "Usage: /etc/init.d/$SERVICE {start|stop}"
    exit 1
    ;;
esac

exit 0

