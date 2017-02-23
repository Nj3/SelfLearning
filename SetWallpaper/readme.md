#Overview

This will set the bing background as your desktop wallpaper(FULLHD resolution :- 1980x1080). 

## Execution:
Open the terminal where you placed the script, run it by using the below command.

`python3 setting_wallpaper.py`

For windows, to change it daily at 9pm,add the below code in cmd

`schtasks /Create /SC DAILY /TN "SET_BG" /TR "python '<filepath>'" /ST 21:00`
