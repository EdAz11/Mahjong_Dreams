import Classes.tile


class Agent:
    def __init__(self):
        self.agent_hand={
            "dr":0,
            "dg":0,
            "dw":0,
            "1m":0,
            "2m":0,
            "3m":0,
            "4m":0,
            "5m":0,
            "6m":0,
            "7m":0,
            "8m":0,
            "9m":0,
            "1p":0,
            "2p":0,
            "3p":0,
            "4p":0,
            "5p":0,
            "6p":0,
            "7p":0,
            "8p":0,
            "9p":0,
            "1s":0,
            "2s":0,
            "3s":0,
            "4s":0,
            "5s":0,
            "6s":0,
            "7s":0,
            "8s":0,
            "9s":0,
            "we":0,
            "ws":0,
            "ww":0,
            "wn":0,  
        }

        self.known_wall={
            "dr":4,
            "dg":4,
            "dw":4,
            "1m":4,
            "2m":4,
            "3m":4,
            "4m":4,
            "5m":4,
            "6m":4,
            "7m":4,
            "8m":4,
            "9m":4,
            "1p":4,
            "2p":4,
            "3p":4,
            "4p":4,
            "5p":4,
            "6p":4,
            "7p":4,
            "8p":4,
            "9p":4,
            "1s":4,
            "2s":4,
            "3s":4,
            "4s":4,
            "5s":4,
            "6s":4,
            "7s":4,
            "8s":4,
            "9s":4,
            "we":4,
            "ws":4,
            "ww":4,
            "wn":4,  
        }



#removes tile from the wall, places tile on hand
def drawn_tile(self, tile):
    #for dragons
    if tile.suit=="dragon":
        if tile.value=="green":
            self.agent_hand["dg"]+=1
            self.known_wall["dg"]-=1
        if tile.value=="red":
            self.agent_hand["dr"]+=1
            self.known_wall["dr"]-=1
        if tile.value=="white":
            self.agent_hand["dw"]+=1
            self.known_wall["dw"]-=1
    #for manzu tiles
    if tile.suit=="manzu":
        if tile.value== 1:
            self.agent_hand["1m"]+=1
            self.known_wall["1m"]-=1
        if tile.value== 2:
            self.agent_hand["2m"]+=1
            self.known_wall["2m"]-=1
        if tile.value== 3:
            self.agent_hand["3m"]+=1
            self.known_wall["3m"]-=1
        if tile.value== 4:
            self.agent_hand["4m"]+=1
            self.known_wall["4m"]-=1
        if tile.value== 5:
            self.agent_hand["5m"]+=1
            self.known_wall["5m"]-=1
        if tile.value== 6:
            self.agent_hand["6m"]+=1
            self.known_wall["6m"]-=1
        if tile.value== 7:
            self.agent_hand["7m"]+=1
            self.known_wall["7m"]-=1
        if tile.value== 8:
            self.agent_hand["8m"]+=1
            self.known_wall["8m"]-=1
        if tile.value== 9:
            self.agent_hand["9m"]+=1
            self.known_wall["9m"]-=1
    #for pinzu tiles
    if tile.suit=="pinzu":
        if tile.value== 1:
            self.agent_hand["1p"]+=1
            self.known_wall["1p"]-=1
        if tile.value== 2:
            self.agent_hand["2p"]+=1
            self.known_wall["2p"]-=1
        if tile.value== 3:
            self.agent_hand["3p"]+=1
            self.known_wall["3p"]-=1
        if tile.value== 4:
            self.agent_hand["4p"]+=1
            self.known_wall["4p"]-=1
        if tile.value== 5:
            self.agent_hand["5p"]+=1
            self.known_wall["5p"]-=1
        if tile.value== 6:
            self.agent_hand["6p"]+=1
            self.known_wall["6p"]-=1
        if tile.value== 7:
            self.agent_hand["7p"]+=1
            self.known_wall["7p"]-=1
        if tile.value== 8:
            self.agent_hand["8p"]+=1
            self.known_wall["8p"]-=1
        if tile.value== 9:
            self.agent_hand["9p"]+=1
            self.known_wall["9p"]-=1
    #for wind tiles
    if tile.suit=="wind":
        if tile.value=="east":
            self.agent_hand["we"]+=1
            self.known_wall["we"]-=1
        if tile.value=="south":
            self.agent_hand["ws"]+=1
            self.known_wall["ws"]-=1
        if tile.value=="west":
            self.agent_hand["ww"]+=1
            self.known_wall["ww"]-=1
        if tile.value=="north":
            self.agent_hand["wn"]+=1
            self.known_wall["wn"]-=1

def discard_tile(self,key):
    #maybe force major negative feedback if tile doesn't exist on hand
    if self.agent_hand[key]==0:
        return 
    else:
        self.agent_hand[key]-=1

def action(self, state):
    pass