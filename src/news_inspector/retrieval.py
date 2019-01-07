from abc import abstractmethod

from news_inspector.core import Trainable


class Retriever(Trainable):
    """
    Retriever abstract class
    """
    
    @abstractmethod
    def retrieve(self, text):
        pass    


class LocationRetriever(Retriever):

     def learn(self, config):     
         pass

     def retrieve(self, text):
         return []

    
