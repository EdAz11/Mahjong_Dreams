

class Neuron:
    
    def __init__(self, x, y=1):
        self.x = x
        self.y=y
        index=0
        
        for i in range(0, x.length):
            self.x[index] = x[i]
            index+=1
            
        #negative entry for TETA weight

#x[0] to x[13] are hand tiles + draw / x[0] hand dictionary x[1] drawn tile
#x[14] is the wall dictionary / x[2] wall dictionary