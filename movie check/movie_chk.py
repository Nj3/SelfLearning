from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
import time
import sys
import http.client

def send_mail(mov,email,pswd):
    """when the movie is found, it will call this function which will send a mail"""
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.login(email,pswd)
        msg = " The movie " + mov + " is available in bookmyshow. book it fast before it ends"
        server.sendmail(email,email, msg)
        server.close()
    except:
        print("Error sending an email")


if __name__ == '__main__':
    # mov = input("Enter the name of the movie:")  # Enter your name of the movie with correct spelling and init format and spaces between each words.
    mov = sys.argv[1] # for entering movie in commandline
    city = sys.argv[2]
    city = city.lower()
    city = city.replace(" ", "-") # mainly for capturing delhi
    mov2 = mov.replace(" ", "-")
    mov2 = mov2.replace(":", "")
    email = sys.argv[3]
    pswd =  sys.argv[4]
    base_url = "https://in.bookmyshow.com/" + city + "/movies/nowshowing"
    while 1:
        try:
            r = urlopen(base_url).read()
        except http.client.IncompleteRead as e:  # exception raised as it has something to do with HTTP protocol
            r = e.partial
        soup = BeautifulSoup(r, 'html.parser')
        # print(soup)
        tag = soup.find('div', {'data-search-filter': 'movies-' + mov2})
        # print(tag)
        if tag is not None:
            send_mail(mov,email,pswd)
            # print("found")
            sys.exit(0)
        else:
            time.sleep(1800)
#            print("sleep check completed successfully. Exiting.....")
#            sys.exit(0)
