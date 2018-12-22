from abc import abstractmethod

from news_inspector.core import Trainable

class KnowledgeBase(Trainable):
    
    @abstractmethod
    def makeGraph(self, array):
        pass    


class KBGraph:
    
    def __init__(self):
        pass


class NaiveKnowledgeBase(KnowledgeBase):

    def learn(self, config):
        pass

    def makeGraph(self, array):
        return KBGraph() 
