import urllib
#import CHNAME

Url = 'https://sites.google.com/'
Channel_img = '/arabicchannelslogos/'
code = 'site'  
txt= '.txt'
ext= '.jpg'
Channel_path = '/arabicstreamtest/'
IMG = (Url + code + Channel_img)



channels = (['LBC','MTV','Aljadeed'])












for channel in channels:
    
    response = (Url + code + Channel_path + channel + txt)
    html = response
    response = urllib.urlopen(html)
    html1 = response.read()
    CHANN = (html1)
    
    print CHANN