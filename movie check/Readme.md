#Overview

This is for checking whether a movie booking is opened online. If it's opened, you will receive a mail notification.

## Pre-requisite:

* Python 3.5
* BeautifulSoup (third party module)(it's available by default in linux)
* gmail account(less secure apps settings Turned on)

## Instructions:

If python is added in your environment variable, run the below command in cmd

`start /B python <python script-path&file> <name of the movie> <city name> <email> <password>`

Otherwise,

`start /B <python.exe path> <python script path & file> <name of the movie> <city name> <email> <password>`

**Note:**
This script will check for the movie every 1hour
in case if the movie name/city has spaces in between, use double quotes for name of the movie/city. Also its for windows. For ubuntu just type the same command without `start /B`
For example,

`python3 ~/blabla/movie_chk.py "xXx: Return of Xander Cage" chennai bla@gmail.com blabla`
