from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import os
import datetime
import platform
import ctypes


def set_wp(path):
    """After downloading the image from the site. It sets the image as desktop wallpaper.
    path tells the url for the image to be downloaded.For ubuntu"""
    nam = str(datetime.datetime.now().date())+'_bing.jpg'
    # print(nam)
    urlretrieve(path, nam) # it saves the wallpaper in project folder
    os.system('gsettings set org.gnome.desktop.background picture-uri file://'+'/home/$USER/PycharmProjects/self_learning/'+nam)

def set_bg(path):
    """After downloading the image from the site. save it in picture folder
     and sets the image as background. for windows"""
    nam = os.path.join("C:\\Users\\natar_000\Pictures\Bing_Wallpapers\\",str(datetime.datetime.now().date())+'_bing.jpg')
    # print(nam)
    urlretrieve(path, nam)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, nam, 3)

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
    if platform.system() == 'Windows':
        set_bg(img_url+res)
    else:
        set_wp(img_url+res)
