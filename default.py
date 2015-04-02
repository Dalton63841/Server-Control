import xbmc
import xbmcaddon
import xbmcgui

__addon__ = xbmcaddon.Addon()
cmd = os.path.join(__addon__.getAddonInfo('path'), 'shutdown.py')

dialog = xbmcgui.Dialog()
call = dialog.select('What would you like to do?', ['Server Power', 'Send Command'])
        # dialog.selectreturns
        #   0 -> escape pressed
        #   1 -> first item
        #   2 -> second item
    if call == 1:
        cmd
    elif call == 2:
        ###add command here for commands
    else:
        ###log failure
