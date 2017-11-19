# Overview

This is for checking whether a movie booking is opened online. If it's opened, you will receive a mail notification.

## Pre-requisite:

* Python 3.5+ - Ensure python is added in PATH Environment Variable.
* BeautifulSoup4 - if not available, install it using `pip install beautifulsoup4`
* gmail account - less secure apps settings turned on only when this script is executing.

## Instructions:

1. Navigate to your folder where the python script is placed and run `python movie_chk.py <movie name in double quotes and each word should begin with capital letter> <city> <email> <password>`
example: `python movie_chk.py "Thor: Ragnarok" Mumbai bla@gmail.com blabla`

**Note:**
This script will check for the movie booking opening every 30mins from the start of execution.
