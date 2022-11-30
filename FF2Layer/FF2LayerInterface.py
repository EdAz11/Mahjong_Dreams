import Classes.player as pl
import FF2Layer.Neuron as neun
import FF2Layer.FF2Layer as ff2
import random

class NetworkInterface():



    n_entries = 15
    n_exits = 14

    def __init__(self, hand, drawn_tile, available_tiles, trainmode=0):
        self.network = ff2.FF2Layer(self.n_entries, 6, self.n_exits)

        self.player = pl.Player(hand, drawn_tile)
        self.known_tiles =hand
        self.known_tiles.append(drawn_tile)
        self.known_tiles.append(available_tiles)
        self.mode=trainmode
        self.situationExamples= self.neuronExamples()

        self.available_tiles =available_tiles
    
    def update(self):
        
        recomendedAction = recomendedAction(self.known_tiles)

        neuron = neun.Neuron(self.known_tiles, recomendedAction)

        #TODO make example neuros for simple cases (ie. 2->2 or sequence situations)
        exampleSent= self.searchExample()

        if self.mode:
            action = self.network.train_network(neuron, exampleSent, 0.1, 0.1)
        else:
            action = self.network.networkResultCalc(neuron.x)
        
        return action
    

    def recomendedResult(tiles_list):
        dict = {}
        index=0
        #index hand tiles into dict
        for tile in tiles_list:
            while (index<14):
                try:
                    dict[tile] +=1
                except:
                    dict[tile] = 1
                index+=1
            break
            #discard tiles on non recomended sequences and trios
            #else discard draw tile
        for key in dict.keys:
            if dict[key] == 1 & tiles_list[key+14-1] <=1 & tiles_list[key+14+1] <=1 & dict[key-1]<1 & dict[key+1]<1:
                return key

            elif dict[key] == 1 & tiles_list[key+14] <=2:
                return key

            elif dict[key] == 4:
                return key

            else:
                return 13

    def saveTraining(self):
        self.network.train_network()

    def neuronExamples():
        examples = []

        examples.append(neun.Neuron([1,4,8,9,17,21,24,26,28,28,31,31,31,32,
        1,4,4,             #1-3 dragons
        3,4,2,3,2,3,3,1,3, #4-12 manzu
        2,4,3,3,3,2,1,3,2, #13-21 pinzu
        4,3,2,3,4,2,0,0,0, #22-30 souzu
        0,3,2,3],1))       #31-34 winds
        examples.append(neun.Neuron([1,1,2,5,7,14,20,22,26,30,32,32,34,34,
        2,1,4,             #1-3 dragons
        3,3,2,3,2,3,3,1,3, #4-12 manzu
        2,2,3,3,3,2,1,3,2, #13-21 pinzu
        4,3,2,3,4,2,0,0,0, #22-30 souzu
        0,3,2,3],2))        #31-34 winds
        examples.append(neun.Neuron([3,5,5,5,8,9,14,14,14,19,20,21,24,25,
        3,4,1,             #1-3 dragons
        0,1,0,4,3,2,4,3,2, #4-12 manzu
        4,0,0,0,0,0,0,0,0, #13-21 pinzu
        0,4,0,0,4,0,0,0,0, #22-30 souzu
        2,2,0,3],3))       #31-34 winds
        examples.append(neun.Neuron([4,5,5,6,8,8,19,20,21,25,31,34,34,34,
        3,3,3,             #1-3 dragons
        1,0,0,0,1,0,3,2,4, #4-12 manzu
        1,2,4,3,0,0,0,0,0, #13-21 pinzu
        0,4,2,3,2,3,1,2,4, #22-30 souzu
        2,1,0,1],5))       #31-34 winds
        examples.append(neun.Neuron([2,2,3,3,3,17,18,20,25,26,27,35,35,35,
        3,1,1,             #1-3 dragons
        1,2,3,4,3,2,3,1,2, #4-12 manzu
        2,3,1,0,1,3,2,3,0, #13-21 pinzu
        4,2,3,0,1,0,1,3,1, #22-30 souzu
        3,4,0,1],17))      #31-34 winds
        examples.append(neun.Neuron([2,2,3,3,4,5,6,23,24,25,29,30,33,33,
        3,1,2,             #1-3 dragons
        0,3,2,0,3,0,0,3,0, #4-12 manzu
        0,2,0,2,0,1,0,0,4, #13-21 pinzu
        1,0,0,3,0,1,0,1,3, #22-30 souzu
        2,2,2,1],29))      #31-34 winds
        examples.append(neun.Neuron([2,2,2,5,5,6,6,7,7,20,20,35,35,36,
        3,0,4,             #1-3 dragons
        1,1,2,1,0,4,0,5,0, #4-12 manzu
        2,3,4,4,4,1,2,3,4, #13-21 pinzu
        3,2,1,3,0,2,0,1,2, #22-30 souzu
        0,2,2,1],34))      #31-34 winds

        return examples

    def searchExample(self):
        toSend = self.situationExamples[0]
        i=0

        dict = {}

        for j in range(0,14) :
            try:
                dict[toSend.x[j]] +=1
            except:
                dict[toSend.x[j]] =0

        for n in toSend.x:
            if n<4:
                if toSend.x[i+14]<=1 & dict[n]==1:
                    return toSend.x[random.randint(0, 2)]
            
            if n< 33:
                if (toSend[i-1]== n-1 & (toSend[i+1]== n+1 | toSend[i+2]== n+1 | toSend[i+3]== n+1 | toSend[i+4]== n+1)):
                    if (toSend[i+1])==1:
                        return toSend.x[random.randint(3,5)]

            if n>32:
                if toSend.x[i+14]<=1 & dict[n]==1:
                    return toSend.x[6]
            i+=1