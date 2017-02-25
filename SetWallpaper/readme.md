#Overview

This will set the bing background as your desktop wallpaper(FULLHD resolution :- 1980x1080).The picture will be saved in your Pictures folder.
This will set the bing background as your desktop wallpaper(FULLHD resolution :- 1980x1080). 

## Installation:

###Ubuntu:

If you want to set Wallpaper in an ad-hoc basis, open the terminal where you placed the script and run it by using the below command.

`python3 BingWallpaper.py`

If you want to set wallpaper automatically everday at 7 45am, add the below line in cron file.

1. To edit cron file, open terminal and enter, `crontab -e`
2. Type this line at the start, `#! /bin/bash`
3. At the last line, type
 `45 7 * * * PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-);/usr/bin/python3 ~/PythonProjects/SelfLearning/SetWallpaper/BingWallpaper.py` (last argument is your script path)
4. Save and exit it.

To check whether it's added, type `crontab -l` in terminal.

For Further info on crontab, please refer this [cron examples](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples)

###Windows:

If you want to set Desktop Background in an ad-hoc basis, run the script either in your IDE or in cmd, type `python <script_path>` (assuming $PATH variable is set for python path, if not enter full path for python.exe).

If you want to set it automatically everyday at 7 45am, either run the below command in cmd or set it in task scheduler using this [guide](http://tinyhacker.com/hacks/complete-guide-to-windows-7s-task-scheduler/)

`schtasks /Create /SC DAILY /TN "SET_BG" /TR "python '<script_path>'" /ST 07:45`

To check whether it's added, type `schtasks /Query /TN "SET_BG"`
