from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import os
import datetime
import platform
import ctypes
import time

def set_wp(path):
    """After downloading the image from the site, it saves it in Picture
    folder. It sets the image as desktop wallpaper.
    path tells the url for the image to be downloaded.For ubuntu"""
    nam =  str(datetime.datetime.now().date()) + '_bing.jpg'
    p = os.path.join(os.path.expanduser('~'),'Pictures')
    if not os.path.exists(p):
        os.mkdir(p)
    urlretrieve(path, os.path.join(p, nam)) # it saves the wallpaper in pictures folder
    os.system('gsettings set org.gnome.desktop.background picture-uri file://'+ str(os.path.join(p, nam)))
    clean_old(p)

def set_bg(path):
    """After downloading the image from the site. save it in picture folder
     and sets the image as background. for windows"""
    p = os.path.join(os.path.expanduser('%USERPROFILE%'),'Pictures','Bing_Wallpapers')
    file_name = str(datetime.datetime.now().date())+'_bing.jpg'
    if not os.path.exists(p):
        os.mkdir(p)
    nam = p + '/' + file_name
    urlretrieve(path, nam)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, nam, 3)
    
def clean_old(p):
    """Clean old images so that it doesn't occupy too much space.
    At any point of time only 1 month old images will be kept"""
    currentTime = time.time()
    
    for f in os.listdir(p):
        full_path = os.path.join(p, f)
        creation_time = os.path.getctime(full_path)
        if os.path.isfile(full_path) and f.endswith('_bing.jpg'):
            if ( currentTime - creation_time ) // ( 24 * 3600 ) > 30:
                os.remove(full_path)
        

if __name__ == '__main__':
    base_url = "http://bingwallpaper.com"
    r = urlopen(base_url).read()
    soup = BeautifulSoup(r,'html.parser')
    tag = soup.select('a.cursor_zoom > img')# '>' this will traverse through multiple tags
    img_url = tag[0].get('src')
    img_url = img_url[:len(img_url)-12] # since strings are immutable im removing the resolution part alone, 12 is the value counted backwards
    res = '1920x1080.jpg'
    if platform.system() == 'Windows':
        set_bg(img_url+res)
    else:
        set_wp(img_url+res)
