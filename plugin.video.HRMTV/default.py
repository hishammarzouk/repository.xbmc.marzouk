#Programming by Hisham Khalil Marzouk
#plugin.video.HRMTV
import xbmc
import os
import xbmcgui
import xbmcplugin
import xbmcaddon
import sys
import urllib
import random
import time
rand = random.randint(1, 100000000000)
cid = str(rand)

urllib.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-62036260-1&cid="+ cid +"&t=event&ec=new%20movement&ea=new%20visit&el=entranece1").close
time.sleep = 15   

from xml.dom import minidom
ADDON = xbmcaddon.Addon(id='plugin.video.HRMTV2')
CHOD = open(os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media','logos','code','')+'T.'+ 'jpg','r')
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




