import os, logging, hashlib, traceback, datetime, cPickle
from reqs.twisted.internet.protocol import Protocol
from reqs.twisted.internet import reactor
from core.constants import *
from core.plugins import protocol_plugins
from core.decorators import *
from core.irc_client import ChatBotFactory

class ExtInfoPacketHandler(BaseMinecraftPacketHandler):
    """
    A Handler class for handling extension information.
    """

    packetID = TYPE_EXTINFO

    def handleData(self, packetData, requestID=None):
        pass

    def packData(self, packetData):
        pass

class ExtEntryPacketHandler(BaseMinecraftPacketHandler):
    """
    A Handler class for handling extension entries.
    """

    packetID = TYPE_EXTENTRY

    def handleData(self, packetData, requestID=None):
        pass

    def packData(self, packetData):
        pass