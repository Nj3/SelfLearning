# Overview

This will set the bing background as your desktop wallpaper(FULLHD resolution :- 1980x1080).The picture will be saved in your Pictures folder. It will keep 1-month-old images.

## Pre-requisites:

1. Python3.5+ - added to PATH variable.
2. BeautifulSoup4 - if not available, install it using `pip install beautifulsoup4`

## Usage:

### Ubuntu:

If you want to set Wallpaper on an ad-hoc basis, open the terminal where you placed the script and run it by using the below command.

`python3 BingWallpaper.py`

If you want to set wallpaper automatically every day (say 7 45 am) add the below line in cron file.

1. To edit cron file, open terminal and enter, `crontab -e`
2. Type this line at the start, `#! /bin/bash`
3. At the last line, type
 `45 7 * * * PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-);/usr/bin/python3 ~/PythonProjects/SelfLearning/SetWallpaper/BingWallpaper.py` (last argument is your script path)
4. Save and exit it.

To check whether it's added, type `crontab -l` in the terminal. 
If you want to change the time, just edit the first two numbers accordingly in crontab file. First one is for minutes and second is for hours.

For Further info on crontab, please refer this [cron examples](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples)

In case if it's not working. check whether it's using correct gsettings by typing `which gsettings`. It should point to /usr/bin/gsettings.

If you still get any other error, redirect it to errorlog and send it to me. At the end of cron line, type `> /tmp/errorlog.txt 2>&1`

### Windows:

If you want to set Desktop Background in an ad-hoc basis, run the script either in your IDE or in cmd, type `python <script_path>`.

If you want to set it automatically every day at 7 45 am, either run the below command in cmd or set it in task scheduler using this [guide](http://tinyhacker.com/hacks/complete-guide-to-windows-7s-task-scheduler/)

`schtasks /Create /SC DAILY /TN "SET_BG" /TR "python '<script_path>'" /ST 07:45`

To check whether it's added, type `schtasks /Query /TN "SET_BG"`

If you want to change the time, say 9 pm, type `schtasks /Change /ST 21:00 /TN "SET_BG"` 
