import xbmc
import xbmcaddon
import os
import struct, socket
import sys
import commands

__addon__ = xbmcaddon.Addon()
ipadd = __addon__.getSetting("ipaddress")
user = __addon__.getSetting("username")
command = __addon__.getSetting("command")
icon = __addon__.getAddonInfo('icon')

xbmc.executebuiltin('Notification(Server Tamer,Sending Command to Server,3000,%s)' % icon)
os.system('ssh %s@%s %s ' % (user, ipadd, command))
