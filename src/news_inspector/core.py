from abc import ABC, abstractmethod
import xml.etree.ElementTree as xmlreader
import pickle
import os 

class Trainable(ABC):

    @abstractmethod
    def learn(self, inputs, outputs):
        pass

class TrainingConfig:

    def __init__(self):
        pass

    def loadFromFile(self, filename):
        if not os.path.isfile(filename):
            raise Exception("Fatal error. Training configuration file '"+filename+"' not found.")

        tree = xmlreader.parse(filename)
        root = tree.getroot() 
        self.texts = []
        self.targets = []
        for doc in root.iter('document'):
            text = ""
            with open(doc.attrib['file']) as file:
                text = " ".join(map(lambda x: x.strip(), file.readlines()))
            self.texts.append( text )
            self.targets.append(doc.attrib['target'])
        self.output = root.attrib['output']

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


def train_model(klass, configfile, outputfile):    
    trainable = klass()
    if not isinstance(trainable, Trainable):
        raise Exception(str(klass)+" is not a subclass of Trainable")

    config = load_training_config(configfile)    
    trainable.learn(config)

    pickle.dump(trainable, open(outputfile, "wb" ))


def load_model(model):
    return pickle.load( open(model, "rb"))
