"""
    IdleNPC
	Non-Playable-Characters for IdleRPG
    
"""

# standard libraries
from datetime import date, datetime, timedelta
import random, time, sys, re, urllib2, urllib, pprint, json
from random import choice

# 3rd party modules
from twisted.internet import protocol, reactor
from twisted.words.protocols import irc
from BeautifulSoup import BeautifulSoup
import pywapi

class Bot(irc.IRCClient):

    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        """ need to pull all of this crap into its own function/class """
        t = datetime.now()
        formatted_time = t.strftime("%I:%M:%S")

        user = "%s" % (user.split('!', 1)[0].strip(), )
        if msg[0] == '~':
            try:
                command = msg[1:].lower().split()[0]
                arguments = msg[1:].lower().split()[1:]
            except:
                self.msg(self.factory.channel, 'Invalid arguments')
                return
 
class BotFactory(protocol.ClientFactory):
    protocol = Bot

    def __init__(self, channel, nickname='o_Q'):
        self.channel = channel
        self.nickname = nickname

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)

if __name__ == "__main__":
    reactor.connectTCP('irc.mozor.net', 6667, BotFactory('#mozor', 'o_Q'))
    reactor.run()