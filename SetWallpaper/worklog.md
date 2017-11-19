`45 7 * * * PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-);/usr/bin/python3 ~/PythonProjects/SelfLearning/SetWallpaper/BingWallpaper.py` (last argument is your script path)

## Explanation:
1. It assigns gnome-session to PID variable.
2. /proc/$PID/environ will contain process current environment.
3. we are cutting the value from second field till the end of each line where the delimiter is '='
4. Then we assign the resultant value to DBUS_SESSION_BUS_ADDRESS since crontab won't tell that it's you who logged in. Hence we need to set this environ variable inside cron.