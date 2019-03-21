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
            raise Exception("Fatal error. Training configuration file '"+filename+"' in folder'"+os.path.dirname(os.path.abspath(filename))+"' not found.")

        tree = xmlreader.parse(filename)
        root = tree.getroot() 
        self.texts = []
        self.targets = []
        for doc in root.iter('document'):
            text = ""
            if not os.path.isfile(doc.attrib['file']): 
                raise Exception("Error. Document '"+doc.attrib['file']+"' in '"+filename+"' was not found. Looking in folder in folder '"+os.path.dirname(os.path.abspath(doc.attrib['file']))+"'. Skipping it.")
            else:
                encoding = "utf-8"
                try: 
                    encoding = doc.attrib['encoding']
                except: pass
                with open(doc.attrib['file'], encoding="ISO-8859-1") as file:
                    text = " ".join(map(lambda x: x.strip(), file.readlines()))
                self.texts.append( text )
                try: 
                    self.targets.append( doc.attrib['target'] )
                except: pass  
        #self.output = root.attrib['output']

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


def load_model(filename):
    with open(filename, "rb") as file:
       return pickle.load(file)

