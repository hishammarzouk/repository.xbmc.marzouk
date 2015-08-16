#Programming by Hisham Khalil Marzouk
#plugin.video.HRMTV2
# Dont do anything
import xbmc
import os
import xbmcgui
import xbmcplugin
import xbmcaddon
import sys
import urllib
from xml.dom import minidom

ADDON = xbmcaddon.Addon(id='plugin.audio.LebanonRadio')
CHOD = open(os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media','logos','')+'T.'+ 'jpg','r')
CHODD = minidom.parse(CHOD)
CHOD2 = CHODD.getElementsByTagName('item',) 
for CHO in CHOD2:
    df1= CHO.attributes['df5'].value
    df2= CHO.attributes['df7'].value
    df3= CHO.attributes['df3'].value
    df4= CHO.attributes['df2'].value
    df5= CHO.attributes['df1'].value
    df6= CHO.attributes['df0'].value
rrl = df1 + df2 + df3 +df4 + df5+ df6
rrl2 = df1 + df2 + df3 +df4 + df5
URL = urllib.urlopen(rrl +'?attredirects=0&d=1')
URLimg = rrl2

CHODD = minidom.parse(URL)
channels = CHODD.getElementsByTagName('item',) 
for channel in channels:
     CHANA = channel.attributes['name'].value 
     CHANP = channel.attributes['channel'].value
     ADDON = xbmcaddon.Addon()
     HANDLE = int(sys.argv[1]) 
     item = xbmcgui.ListItem(CHANA,ADDON.getLocalizedString(30001),iconImage = (URLimg) + CHANA +'.jpg')
     xbmcplugin.addDirectoryItem(HANDLE,(CHANP),item, False)
xbmcplugin.endOfDirectory(HANDLE)        