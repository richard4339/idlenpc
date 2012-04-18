#!/usr/bin/env python

# IdleNPC
# https://github.com/mozor/idlenpc

import socket  
import sys
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('idlenpc.cfg')

server = config.get('IRC', 'server')
port = config.get('IRC', 'port')
channel = config.get('IRC', 'channel')
botnick = config.get('IRC', 'nickname')
master = config.get('IRC', 'idlebot')
char_class = config.get('IRC', 'character_class')
host = config.get('Network', 'local_ip')

def ping(): 
  ircsock.send("PONG :Pong\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

def register(chan):
	ircsock.send("PRIVMSG "+ master +" :REGISTER "+ botnick +" examplepass " + char_class + "\n")

def id(master): 
  ircsock.send("PRIVMSG "+ master +" :LOGIN "+ botnick +" examplepass\n")

ircsock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
ircsock.bind((host, 0))
ircsock.connect((server, port)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Mega Python IdleRPG Master\n")
ircsock.send("NICK "+ botnick +"\n") 
time.sleep(5)

joinchan(channel) 
id(master)

#if sys.argv[2] == "register":
#	register(channel)

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg)

  if ircmsg.find("PING :") != -1:
    ping()
