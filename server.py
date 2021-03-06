from __future__ import print_function

import sys
from time import sleep, localtime
from random import randint
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

class ServerChannel(Channel):
    """
    This is the server representation of a single connected client.
    """
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        self.id = str(self._server.NextId())
        intid = int(self.id)
        self.color = [] 
        self.lines = []
        #self.PassOn(self.id)
    
    def PassOn(self, data):
        # pass on what we received to all connected clients
        data.update({"id": self.id})
        self._server.SendToAll(data)
    
    def Close(self):
        self._server.DelPlayer(self)
    
    ##################################
    ### Network specific callbacks ###
    ##################################
    def Network_newgame(self,data):
        self.PassOn(data)

    def Network_click(self,data):
        print("click2")
        print(data)
        self.PassOn(data)
    

class TicTacToeServer(Server):
    channelClass = ServerChannel
    
    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('Server launched')
    
    def NextId(self):
        self.id += 1
        return self.id
    
    def Connected(self, channel, addr):
        self.AddPlayer(channel)
    
    def AddPlayer(self, player):
        print("New Player" + str(player.addr))
        self.players[player] = True
        self.SendPlayers()
    
    def DelPlayer(self, player):
        print("Deleting Player" + str(player.addr))
        del self.players[player]
        self.SendPlayers()
    
    def SendPlayers(self):
        self.SendToAll({"action": "players", "players": dict([(p.id, p.color) for p in self.players])})
    
    def SendToAll(self, data):
        [p.Send(data) for p in self.players]
    
    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)

# get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = TicTacToeServer(localaddr=(host, int(port)))
        s.Launch()

