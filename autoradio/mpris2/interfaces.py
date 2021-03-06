# -*- coding: UTF8 -*
"""
This is mprisV2.1 documentation

http://www.mpris.org/2.1/spec/index.html
"""

class Interfaces(object):
    """
    This class contains the constants defined at index of MPRIS2 definition:

    
    **Interfaces:**
    
    * MEDIA_PLAYER
        'org.mpris.MediaPlayer2'
    * TRACK_LIST
        'org.mpris.MediaPlayer2.TrackList'
    * PLAYER
        'org.mpris.MediaPlayer2.Player'
    * PLAYLISTS
        'org.mpris.MediaPlayer2.Playlists'
    * PROPERTIES
        'org.freedesktop.DBus.Properties'
    

    **Signals:**
    
    * SIGNAL
        'PropertiesChanged'
    

    **Objects:**
    
    * OBJECT_PATH
        '/org/mpris/MediaPlayer2'
    
    """
    #interface
    MEDIA_PLAYER = 'org.mpris.MediaPlayer2'
    TRACK_LIST = 'org.mpris.MediaPlayer2.TrackList'
    PLAYER = 'org.mpris.MediaPlayer2.Player'
    PLAYLISTS = 'org.mpris.MediaPlayer2.Playlists'
    PROPERTIES = 'org.freedesktop.DBus.Properties'
    #signal
    SIGNAL = 'PropertiesChanged'
    #Object
    OBJECT_PATH = '/org/mpris/MediaPlayer2'
    
    