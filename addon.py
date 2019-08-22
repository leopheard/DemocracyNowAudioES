from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL1 = "https://www.democracynow.org/podcast-es.xml"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://assets.democracynow.org/assets/DN-Podcast-ESPANOL-9dd56c747e3ab3179fc42d2a2f2dda4911d9d3fed479d5169214f97a6ed70b15.jpg"},
 {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://assets.democracynow.org/assets/DN-Podcast-ESPANOL-9dd56c747e3ab3179fc42d2a2f2dda4911d9d3fed479d5169214f97a6ed70b15.jpg"},
    ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
