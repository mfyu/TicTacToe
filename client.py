import sys, math
from time import sleep
from PodSixNet.Connection import connection, ConnectionListener
from TicTacToe import TicTacToe

class Client(ConnectionListener, TicTacToe):
    def __init__(self, host, port):
        self.Connect((host, port))
        self.players = {}
        self.data = []
        self.piece = ""
        TicTacToe.__init__(self)
    
    def Loop(self):
        self.Pump()
        connection.Pump()
        self.Events()
        

    def Click(self, e):
        print(e.pos)
        col = math.floor(e.pos[0]/100)
        row = math.floor(e.pos[1]/100)
        connection.Send({"action": "click", "position": e.pos, "turn" : "x", "row":row, "col": col})

    def newGame(self):

        connection.Send({"action":"newgame"})
    
    ###############################
    ### Network event callbacks ###
    ###############################
    def Network_newgame(self,data):
        print(data)
        self.drawNewBoard()
    def Network_click(self,data):
        print("click")
        print(data)
        self.Turn(data)
   
    
    def Network(self, data):
        #print('network:', data)
        pass
    
    def Network_connected(self, data):
        self.statusLabel = "connected"
        print("CONNECTED")
        print(data)
    
    def Network_error(self, data):
        print(data)
        import traceback
        traceback.print_exc()
        self.statusLabel = data['error'][1]
        connection.Close()
    
    def Network_disconnected(self, data):
        self.statusLabel += " - disconnected"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        c = Client(host, int(port))
        #c = Client("localhost", 12345)
        while 1:
            c.Loop()
            sleep(0.001)