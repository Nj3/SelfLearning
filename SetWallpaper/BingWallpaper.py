from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import os
import datetime


def set_wp(path):
    """After downloading the image from the site. It sets the image as desktop wallpaper.
    path tells the url for the image to be downloaded"""
    nam = str(datetime.datetime.now().date())+'_bing.jpg'
    # print(nam)
    urlretrieve(path, nam) # it saves the wallpaper in project folder
    # os.system('cp ~/PycharmProjects/self_learning/'+nam + ' /home/$USER/Pictures') #it copies the image to picture folder ,it seems only from picture folder i can set the bg
    os.system('gsettings set org.gnome.desktop.background picture-uri file://'+'/home/$USER/PycharmProjects/self_learning/'+nam)

if __name__ == '__main__':
    base_url = "http://bingwallpaper.com"
    r = urlopen(base_url).read()
    soup = BeautifulSoup(r,'html.parser')
    tag = soup.select('a.cursor_zoom > img')# '>' this will traverse through multiple tags
    # print(type(tag))
    img_url = tag[0].get('src')
    # print(img_url)
    img_url = img_url[:len(img_url)-12] # since strings are immutable im removing the resolution part alone, 12 is the value counted backwards
    # print(img_url)
    res = '1920x1080.jpg'
    # print(img_url+res)
    set_wp(img_url+res)