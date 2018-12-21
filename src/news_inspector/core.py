from abc import ABC, abstractmethod
import xml.etree.ElementTree as xmlreader

class Trainable(ABC):

    @abstractmethod
    def learn(self, inputs, outputs):
        pass

class TrainingConfig:

    def __init__(self):
        pass

    def loadFromFile(self, filename):
        tree = xmlreader.parse(filename)
        self.texts = []
        self.targets = []
        self.output = ""

    def getTexts(self):
        return self.texts

    def getTargets(self):
        return self.targets
 
    def getOutputFileName(self):
        return self.output

def load_training_config(filename):
    resp = TrainingConfig() 
    resp.loadFromFile(filename)
    return resp


def train_model(klass, configfile):    
    trainable = klass()
    if not isinstance(trainable, Trainable):
        raise Exception(str(klass)+" is not a subclass of Trainable")

    config = load_training_config(configfile)    
    trainable.learn(config)


def load_model(model):
    pass
