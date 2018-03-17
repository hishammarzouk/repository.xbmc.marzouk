#Youtube channels
#
#
#
#
#
#Hisham Marzouk
import re
import os
import sys
import urllib2
import buggalo
import xbmcgui
import xbmcaddon
import xbmcplugin
import random
rand = random.randint(1, 100000000000)
cid = str(rand)

urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-63789805-1&cid="+ cid +"&t=event&ec=new%20movement&ea=new%20visit&el=entranece1").close

BASE_URL = 'https://sites.google.com/site/milamouseaddon/'
PLAY_VIDEO_PATH = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
PLAYLIST_PATH = 'plugin://plugin.video.youtube/channel/UC7Lo9mbZbtSc8kIbxRN8uLg/'
PLAYLIST_PATH1 = 'plugin://plugin.video.youtube/channel/UCfaNp0IpqyArhTgUfmWc6Lg/'
PLAYLIST_PATH2 = 'plugin://plugin.video.youtube/channel/UCsmbbaUAxCk8V-b7VKdYlmw/'
PLAYLIST_PATH3 = 'plugin://plugin.video.youtube/channel/UC58fPf-h93d4fPoFBUd3NMA/'
PLAYLIST_PATH4 = 'plugin://plugin.video.youtube/channel/UCO8cb9wxi0u1tIyujHxB85w/'
PLAYLIST_PATH5 = 'plugin://plugin.video.youtube/channel/UCkAGrHCLFmlK3H2kd6isipg/'
PLAYLIST_PATH6 = 'plugin://plugin.video.youtube/channel/UCD3evZG8u9raYYvelvCfNtw/'
PLAYLIST_PATH7 = 'plugin://plugin.video.youtube/channel/UCtUTgfvms3d2SdrnMS0c5Ag/'
PLAYLIST_PATH8 = 'plugin://plugin.video.youtube/channel/UCJPCbjlEoYOQKQDg7qRvDtQ/'




if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])

    try:
        u = urllib2.urlopen(BASE_URL)
        html = u.read()
        u.close()


        m = re.search('//www.youtube.com/embed/([^"]+)"', html, re.DOTALL)
        if m:
            item = xbmcgui.ListItem('Mickey Mouse Wunderhause',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-p5hQVOAShhU/AAAAAAAAAAI/AAAAAAAAAAA/-dVwa_GtXEE/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH, item, True)
         
            item = xbmcgui.ListItem('Sofia die Erste DeutschTV',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-MGtui0Kzv5c/AAAAAAAAAAI/AAAAAAAAAAA/6kTGKtuueCM/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH1, item, True)
         
            item = xbmcgui.ListItem('Henry Knuddelmonster',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-gqgZKr_ezw4/AAAAAAAAAAI/AAAAAAAAAAA/P_qL5NvuXq8/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH2, item, True)

            item = xbmcgui.ListItem('SurpriseEggs4Kids',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-8IesUEuPj14/AAAAAAAAAAI/AAAAAAAAAAA/MGbwjuYVjgE/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH3, item, True)
            item = xbmcgui.ListItem(' Deutsch - Die Helden der Stadt',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-Ik-kcqGqufc/AAAAAAAAAAI/AAAAAAAAAAA/ldhhtndcMMo/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH4, item, True)
            item = xbmcgui.ListItem('Mr. Bean',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-FvBjR0DHn0c/AAAAAAAAAAI/AAAAAAAAAAA/1X7Fl-w2PUw/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH5, item, True)
            item = xbmcgui.ListItem('Mr. Cartoon',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-fatWygraRUQ/AAAAAAAAAAI/AAAAAAAAAAA/psF5YKQTVeY/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH6, item, True)
            item = xbmcgui.ListItem('Tom and Jerry Cartoons',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-Vr4tx025RcQ/AAAAAAAAAAI/AAAAAAAAAAA/LCEiC93FeYg/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH7, item, True)
            item = xbmcgui.ListItem(' Entspannungsmusik',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-Ide6mlCfkvE/AAAAAAAAAAI/AAAAAAAAAAA/Z5Jr1vpepPY/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH8, item, True)
            
            

         
        xbmcplugin.endOfDirectory(HANDLE)
    except:
        buggalo.onExceptionRaised()
