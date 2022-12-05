import os
import random
import FF2Layer.SigmoidFn as sgf
import pickle

class FF2Layer():

    def __init__(self, n_entries=2, layer_size=5, n_exits=14):
        
        self.n_entries =n_entries
        self.layer_size1=layer_size
        self.n_exits =n_exits

        seed = os.getpid()
        
        #weight matrix for the first layer
        
        self.weights1 = [] #[n_entries+1][layer_size]
        self.weights2 = [] #[layer_size+1][n_exits]
        
        self.activation1= [] #[layer_size1+1]
        self.activation_hidden=[] #[n_exits]
        self.error_hidden=[] #error_hidden[layer_size1+ 1]
        self.error_exit=[]
        
        self.max_interations=10000
        
        self.loadWeights()

    def forwardPropagation(self,instance): #argument is a list of doubles
        sum=0
        result=0

        output=-1

        #first layer calc
        for i in range(0, self.layer_size1):
            for j in range(0, self.n_entries):
                sum += self.weights1[j][i]*instance[j]

            self.activation1[i] = sgf.output(sum+ self.error_exit[i])

        self.activation1[self.layer_size1] = -1

        sum=0
        #exit layer calculation

        for i in range(0, self.n_exits):
            for j in range(0, self.layer_size1):
                sum += self.activation1[j]* self.weights2[j][i]
            self.activation_hidden[i] = sgf.output(sum)

        for i in range(0, self.n_exits):
            result=self.activation_hidden[i]
            output = i
        
        return output+1

    def backPropagation(self, neuron):
        for i in range(0, self.n_exits):
            self.error_exit[i] = sgf.derivative(self.activation_hidden[i])
        
        #error calculation for hidden layer units
        for i in range(0, self.layer_size1+1):
            sum=0
            for j in range(0, self.n_exits):
                sum+= self.weights2[i][j] * self.error_exit[j]
            self.error_hidden[i] = sgf.derivative(self.activation1[i])*sum

        #exit layer weight update
        for i in range(0, self.n_exits):
            for j in range(0, self.layer_size1+1):
                self.weights2[j][i] += self.alpha*self.error_exit[i]*self.activation1[j]

        #hidden layer weight update
        for i in range(0, self.n_exits):
            for j in range(0, self.layer_size1+1):
                self.weights1[j][i]+= self.alpha * self.error_hidden[i]* neuron.x[j]

    def train_network(self, neuronTrainingSet, neuronTestSet, alpha, errorLimit):
        self.alpha = alpha,
        self.error_limit= errorLimit
        
        for i in range(0, self.n_entries+1):
            for j in range(0, self.n_entries):
                if random.randint(0,2)==0:
                    self.weights1[i][j] = random.random()
                else:
                    self.weights1[i][j] = -random.random()
                    
        for i in range(0, self.layer_size1+1):
            for j in range(0, self.n_exits):
                if random.randint(0,2)==0:
                    self.weights2[i][j] = random.random()
                else:
                    self.weights2[i][j] = -random.random()

        result = self.forwardPropagation(neuronTrainingSet)
        self.backPropagation(neuronTrainingSet)

        return result

    def saveWeights(self):

        pickle.dump(self.weights1, open('/weights1.p', 'wb'))
        pickle.dump(self.weights2, open('/weights2.p', 'wb'))
        pickle.dump(self.error_exit, open('/error_exit.p', 'wb'))
        pickle.dump(self.error_hidden, open('/error_hidden.p', 'wb'))
        pickle.dump(self.activation1, open('/activation1.p', 'wb'))
        pickle.dump(self.activation_hidden, open('/activation_hidden.p', 'wb'))

    def loadWeights(self):

        self.weights1 = pickle.load(open('/weights1.p', 'rb'))
        self.weights2 = pickle.load(open('/weights2.p', 'rb'))
        self.error_exit= pickle.load(self.error_exit, open('/error_exit.p', 'rb'))
        self.error_hidden = pickle.load(self.error_hidden, open('/error_hidden.p', 'rb'))
        self.activation1 = pickle.load(self.activation1, open('/activation1.p', 'rb'))
        self.activation_hidden = pickle.load(self.activation_hidden, open('/activation_hidden.p', 'rb'))


    def networkResultCalc(self, instance):
        return int(self.forwardPropagation(instance))