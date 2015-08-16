from xbmcswift2 import Plugin
from xml.dom import minidom
import urllib


Link = "https://sites.google.com/site/projectghorba/"  
thumb = "https://sites.google.com/site/projectghorba/home/logos/"
CHOD = urllib.urlopen(Link+'live.xml')
CHODD = minidom.parse(CHOD)
channels = CHODD.getElementsByTagName('item',) 

Allchannes = urllib.urlopen(Link+'allchannels.xml')
Allchan = minidom.parse(Allchannes)
lebchannels = Allchan.getElementsByTagName('lebanon',) 
syrichannels = Allchan.getElementsByTagName('syria',)
egychannels = Allchan.getElementsByTagName('egypt',)
tunchannels = Allchan.getElementsByTagName('tunis',)
algchannels = Allchan.getElementsByTagName('algeria',)
irachannels = Allchan.getElementsByTagName('iraq',)
jorchannels = Allchan.getElementsByTagName('jordan',)
emichannels = Allchan.getElementsByTagName('emirates',)
kuwchannels = Allchan.getElementsByTagName('kuwait',)
libchannels = Allchan.getElementsByTagName('libya',)
morchannels = Allchan.getElementsByTagName('morocco',)
omachannels = Allchan.getElementsByTagName('oman',)
palchannels = Allchan.getElementsByTagName('palestinian',)
qatchannels = Allchan.getElementsByTagName('qatar',)
bahchannels = Allchan.getElementsByTagName('bahrain',)
sudchannels = Allchan.getElementsByTagName('sudan',)
sauchannels = Allchan.getElementsByTagName('saudi',)
yemchannels = Allchan.getElementsByTagName('yeman',)




YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'






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
    items = [{'label': _("LIVE"),'path': plugin.url_for('show_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/LIVE.png?attredirects=0&d=1") },
    {'label': _("LEBANON"),'path': plugin.url_for('leb_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/lebanon.png?attredirects=0&d=1") },
    {'label': _("Syria"),'path': plugin.url_for('syr_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/syria.png?attredirects=0&d=1") },
    {'label': _("Egypt"),'path': plugin.url_for('egy_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/egypt.png?attredirects=0&d=1")},
	{'label': _("Iraq"),'path': plugin.url_for('ira_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/iraq.png?attredirects=0&d=1")},
    {'label': _("Tunis"),'path': plugin.url_for('tun_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/tunis.png?attredirects=0&d=1")},
    {'label': _("Algeria"),'path': plugin.url_for('alg_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/algeria.png?attredirects=0&d=1")},
	{'label': _("Jordan"),'path': plugin.url_for('jor_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/jordan.png?attredirects=0&d=1") },
    {'label': _("Emirates"),'path': plugin.url_for('emi_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/emirates.png?attredirects=0&d=1") },
    {'label': _("Kuwait"),'path': plugin.url_for('kuw_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/kuwait.png?attredirects=0&d=1") },
    {'label': _("Libya"),'path': plugin.url_for('lib_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/libya.png?attredirects=0&d=1")},
	{'label': _("Morocco"),'path': plugin.url_for('mor_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/morocco.png?attredirects=0&d=1") },
    {'label': _("Oman"),'path': plugin.url_for('oma_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/oman.png?attredirects=0&d=1") },
    {'label': _("Palestinian"),'path': plugin.url_for('pal_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/palestinian.png?attredirects=0&d=1") },
    {'label': _("Qatar"),'path': plugin.url_for('qat_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/qatar.png?attredirects=0&d=1")},
     {'label': _("Bahrain"),'path': plugin.url_for('bah_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/bahrain.png?attredirects=0&d=1")},
	{'label': _("Sudan"),'path': plugin.url_for('sud_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/sudan.png?attredirects=0&d=1") },
    {'label': _("Saudi"),'path': plugin.url_for('sau_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/saudi.png?attredirects=0&d=1") },
    {'label': _("Yemen"),'path': plugin.url_for('yem_channels'),
    'thumbnail':("https://sites.google.com/site/projectghorba/home/logos/yemen.png?attredirects=0&d=1")}]
    return plugin.finish(items)





@plugin.route("/Live/")
def show_channels():
    items = [{
        'label':channel.attributes['name'].value,
        'path': channel.attributes['channel'].value,
        'thumbnail':thumb+ channel.attributes['name'].value,
        'is_playable': True,
    } for channel in channels]
    return plugin.finish(items)

@plugin.route('/LEBANON/')

def leb_channels():
    items = [{
        'label':lebchannel.attributes['name'].value,
        'thumbnail':thumb+ lebchannel.attributes['name'].value,
        'path': YOUTUBE_URL % lebchannel.attributes['channel'].value,
    } for lebchannel in lebchannels]
    return plugin.finish(items)

@plugin.route('/Syria/')

def syr_channels():
    items = [{
        'label':syrchannel.attributes['name'].value,
        'thumbnail':thumb+ syrchannel.attributes['name'].value,
        'path': YOUTUBE_URL % syrchannel.attributes['channel'].value,
    } for syrchannel in syrichannels]
    return plugin.finish(items)

@plugin.route('/Egypt/')
def egy_channels():
    items = [{
        'label':egychannel.attributes['name'].value,
        'thumbnail':thumb+ egychannel.attributes['name'].value,
        'path': YOUTUBE_URL % egychannel.attributes['channel'].value,
    } for egychannel in egychannels]
    return plugin.finish(items)


@plugin.route('/Iraq/')
def ira_channels():
    items = [{
        'label':irchannel.attributes['name'].value,
        'thumbnail':thumb+ irchannel.attributes['name'].value,
        'path': YOUTUBE_URL % irchannel.attributes['channel'].value,
    } for irchannel in irachannels]
    return plugin.finish(items)


@plugin.route('/Tunis/')
def tun_channels():
    items = [{
        'label':tunichannel.attributes['name'].value,
        'thumbnail':thumb+ tunichannel.attributes['name'].value,
        'path': YOUTUBE_URL % tunichannel.attributes['channel'].value,
    } for tunichannel in tunchannels]
    return plugin.finish(items)


@plugin.route('/Algeria/')
def alg_channels():
    items = [{
        'label':algechannel.attributes['name'].value,
        'thumbnail':thumb+ algechannel.attributes['name'].value,
        'path': YOUTUBE_URL % algechannel.attributes['channel'].value,
    } for algechannel in algchannels]
    return plugin.finish(items)


@plugin.route('/Jordan/')
def jor_channels():
    items = [{
        'label':Jordchannel.attributes['name'].value,
        'thumbnail':thumb+ Jordchannel.attributes['name'].value,
        'path': YOUTUBE_URL % Jordchannel.attributes['channel'].value,
    } for Jordchannel in jorchannels]
    return plugin.finish(items)

@plugin.route('/Kuwait/')
def kuw_channels():
    items = [{
        'label':kuwachannel.attributes['name'].value,
        'thumbnail':thumb+ kuwachannel.attributes['name'].value,
        'path': YOUTUBE_URL % kuwachannel.attributes['channel'].value,
    } for kuwachannel in kuwchannels]
    return plugin.finish(items)

@plugin.route('/Libya/')
def lib_channels():
    items = [{
        'label':libychannel.attributes['name'].value,
        'thumbnail':thumb+ libychannel.attributes['name'].value,
        'path': YOUTUBE_URL % libychannel.attributes['channel'].value,
    } for libychannel in libchannels]
    return plugin.finish(items)

@plugin.route('/Morocco/')
def mor_channels():
    items = [{
        'label':moroychannel.attributes['name'].value,
        'thumbnail':thumb+ moroychannel.attributes['name'].value,
        'path': YOUTUBE_URL % moroychannel.attributes['channel'].value,
    } for moroychannel in morchannels]
    return plugin.finish(items)


@plugin.route('/Oman/')
def oma_channels():
    items = [{
        'label':omanchannel.attributes['name'].value,
        'thumbnail':thumb+ omanchannel.attributes['name'].value,
        'path': YOUTUBE_URL % omanchannel.attributes['channel'].value,
    } for omanchannel in omachannels]
    return plugin.finish(items)


@plugin.route('/Palestinian/')
def pal_channels():
    items = [{
        'label':palechannel.attributes['name'].value,
        'thumbnail':thumb+ palechannel.attributes['name'].value,
        'path': YOUTUBE_URL % palechannel.attributes['channel'].value,
    } for palechannel in palchannels]
    return plugin.finish(items)




@plugin.route('/Qatar/')
def qat_channels():
    items = [{
        'label':qatachannel.attributes['name'].value,
        'thumbnail':thumb+ qatachannel.attributes['name'].value,
        'path': YOUTUBE_URL % qatachannel.attributes['channel'].value,
    } for qatachannel in qatchannels]
    return plugin.finish(items)

@plugin.route('/Bahrain/')
def bah_channels():
    items = [{
        'label':bahrchannel.attributes['name'].value,
        'thumbnail':thumb+ bahrchannel.attributes['name'].value,
        'path': YOUTUBE_URL % bahrchannel.attributes['channel'].value,
    } for bahrchannel in bahchannels]
    return plugin.finish(items)





@plugin.route('/Emirates/')
def emi_channels():
    items = [{
        'label':emirchannel.attributes['name'].value,
        'thumbnail':thumb+ emirchannel.attributes['name'].value,
        'path': YOUTUBE_URL % emirchannel.attributes['channel'].value,
    } for emirchannel in emichannels]
    return plugin.finish(items)




@plugin.route('/Sudan/')
def sud_channels():
    items = [{
        'label':sudachannel.attributes['name'].value,
        'thumbnail':thumb+ sudachannel.attributes['name'].value,
        'path': YOUTUBE_URL % sudachannel.attributes['channel'].value,
    } for sudachannel in sudchannels]
    return plugin.finish(items)


@plugin.route('/Saudi/')
def sau_channels():
    items = [{
        'label':saudchannel.attributes['name'].value,
        'thumbnail':thumb+ saudchannel.attributes['name'].value,
        'path': YOUTUBE_URL % saudchannel.attributes['channel'].value,
    } for saudchannel in sauchannels]
    return plugin.finish(items)

@plugin.route('/Yemen/')
def yem_channels():
    items = [{
        'label':yemechannel.attributes['name'].value,
        'thumbnail':thumb+ yemechannel.attributes['name'].value,
        'path': YOUTUBE_URL % yemechannel.attributes['channel'].value,
    } for yemechannel in yemchannels]
    return plugin.finish(items)


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id

if __name__ == '__main__':
    plugin.run()
