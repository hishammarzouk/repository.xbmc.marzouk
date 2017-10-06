from xbmcswift2 import Plugin
from xml.dom import minidom
import urllib

hrmlink = "https://raw.githubusercontent.com/hishammarzouk/HRMTV/master/LOGOS/"
hrmthumb = "https://raw.githubusercontent.com/hishammarzouk/HRMTV/master/LOGOS/"
Link = "https://raw.githubusercontent.com/hishammarzouk/Ramadan2017/master/" 
thumb = "https://raw.githubusercontent.com/hishammarzouk/Ramadan2017/master/logos/"
#Link = "http://localhost:82/"
#thumb = "http://localhost:82/logos/"
CHOD = urllib.urlopen(hrmlink+'lebanon.jpg')
CHODD = minidom.parse(CHOD)
channels = CHODD.getElementsByTagName('item',) 

Allchannes = urllib.urlopen(Link+'allchannels.xml')
Allchan = minidom.parse(Allchannes)


de7kchannels = Allchan.getElementsByTagName('de7ek',)
arabicchannels = Allchan.getElementsByTagName('arabic',) 
turkchannels = Allchan.getElementsByTagName('turk',) 
aghanichannels = Allchan.getElementsByTagName('aghani',) 
ijtimachannels = Allchan.getElementsByTagName('ijtima',) 
rousumchannels = Allchan.getElementsByTagName('rousum',)
wasakchannels = Allchan.getElementsByTagName('wasak',)

YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

YOUTUBE_URL_list ='plugin://plugin.video.youtube/playlist/%s/'




STRINGS = {
    'page': 30001,
    'channels': 30100,
    'videos': 30101,
    'vodcasts': 30103,
    'search': 30200,
    'name': 30201
}



plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [{'label': _("HRM"),'path': plugin.url_for('show_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/hrm.png?raw=true") },
    {'label': _("برامج مضحكة"),'path': plugin.url_for('de7k_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/funy.png?raw=true") },
    {'label': _("مسلسلات عربية"),'path': plugin.url_for('arabic_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/Amus.png?raw=true") },
    {'label': _("مسلسلات تركية"),'path': plugin.url_for('turk_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/Tmus.png?raw=true") },
	{'label': _("اغاني عربية"),'path': plugin.url_for('aghani_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/music.png?raw=true") },
	{'label': _("برامج اجتماعية"),'path': plugin.url_for('ijtima_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/ijtema.png?raw=true") },
	{'label': _("رسوم متحركة"),'path': plugin.url_for('rousum_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/rusum.png?raw=true") },
	{'label': _("افلام وثائقية"),'path': plugin.url_for('wasak_channels'),
    'thumbnail':("https://github.com/hishammarzouk/Ramadan2017/blob/master/logos/wasak.png?raw=true") }
	
             ]



    return plugin.finish(items)


@plugin.route("/Live/")
def show_channels():
    items = [{
        'label':channel.attributes['name'].value,
        'path': channel.attributes['channel'].value,
        'thumbnail':hrmthumb + channel.attributes['name'].value + ".jpg",
        'is_playable': True,
    } for channel in channels]
    return plugin.finish(items)

@plugin.route('/DE7ek/')
 
def de7k_channels():
    items = [{
        'label':de7kchannel.attributes['name'].value,
        'thumbnail':thumb+ de7kchannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % de7kchannel.attributes['channel'].value,
    } for de7kchannel in de7kchannels]
    return plugin.finish(items)

@plugin.route('/Arabic/')
 
def arabic_channels():
    items = [{
        'label':arabicchannel.attributes['name'].value,
        'thumbnail':thumb+ arabicchannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % arabicchannel.attributes['channel'].value,
    } for arabicchannel in arabicchannels]
    return plugin.finish(items)


@plugin.route('/Turk/')
 
def turk_channels():
    items = [{
        'label':turkchannel.attributes['name'].value,
        'thumbnail':thumb+ turkchannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % turkchannel.attributes['channel'].value,
    } for turkchannel in turkchannels]
    return plugin.finish(items)	
	

	
	
@plugin.route('/Aghani/')
 
def aghani_channels():
    items = [{
        'label':aghanichannel.attributes['name'].value,
        'thumbnail':thumb+ aghanichannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % aghanichannel.attributes['channel'].value,
    } for aghanichannel in aghanichannels]
    return plugin.finish(items)	
	

@plugin.route('/Ijtima/')
 
def ijtima_channels():
    items = [{
        'label':ijtimachannel.attributes['name'].value,
        'thumbnail':thumb+ ijtimachannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % ijtimachannel.attributes['channel'].value,
    } for ijtimachannel in ijtimachannels]
    return plugin.finish(items)	
	

@plugin.route('/Rousum/')
 
def rousum_channels():
    items = [{
        'label':rousumchannel.attributes['name'].value,
        'thumbnail':thumb+ rousumchannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % rousumchannel.attributes['channel'].value,
    } for rousumchannel in rousumchannels]
    return plugin.finish(items)	

@plugin.route('/Wasak/')
 
def wasak_channels():
    items = [{
        'label':wasakchannel.attributes['name'].value,
        'thumbnail':thumb+ wasakchannel.attributes['name'].value + ".jpg",
        'path': YOUTUBE_URL_list % wasakchannel.attributes['channel'].value,
    } for wasakchannel in wasakchannels]
    return plugin.finish(items)	
	
	
	


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id

if __name__ == '__main__':
    plugin.run()
