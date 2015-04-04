import xbmc
import xbmcaddon
import os
import struct, socket
import sys
import commands

__addon__ = xbmcaddon.Addon()
ipadd = __addon__.getSetting("ipaddress")
mac = __addon__.getSetting("macaddress")
user = __addon__.getSetting("username")
command = __addon__.getSetting("command")
icon = __addon__.getAddonInfo('icon')

xbmc.executebuiltin('Notification(Nas Power,Checking Remote Server Status,5000,%s)' % icon)
result = commands.getoutput("ping -c1 " + ipadd)
if result.find("100% packet loss") == -1:
    xbmc.executebuiltin('Notification(Nas Power,Shutting Down Remote Server,3000,%s)' % icon)
    os.system('ssh %s@%s %s ' % (user, ipadd, command))
    result = True
    while (result == True):
        check = commands.getoutput("ping -c1 " + ipadd)
        if check.find("100% packet loss") != -1:
	    result = False
	    xbmc.executebuiltin('Notification(Nas Power,Server has successfully powered off,3000,%s)' % icon)
else:
    xbmc.executebuiltin('Notification(Nas Power,Waking Remote Server,3000,%s)' % icon)
    xbmc.executebuiltin("WakeOnLan(%s)" % mac)
    result = False
    while (result == False):
        check = commands.getoutput("ping -c1 " + ipadd)
        if check.find("100% packet loss") == -1:
            result = True
            xbmc.executebuiltin('Notification(Nas Power,Server has successfully powered on,3000,%s)' % icon)

