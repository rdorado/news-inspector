from abc import ABC, abstractmethod

class Classifier(ABS):
    
     @abstractmethod
     def classify(self, text):
        pass    

    
class PolarityClassifier(Classifier):
    
    def classify(self, text):
        pass
