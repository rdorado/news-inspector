from abc import abstractmethod

from news_inspector.core import Trainable

class KnowledgeBase(Trainable):
    
    @abstractmethod
    def makeGraph(self, array):
        pass    


class Node:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.arcs = {}  # 'type_of_rel': [id1, id2] 
                

        
    def save(repodir):    
        pass
    
class Arc:

    def __init__(self):
        self.target = None
        self.weight = 1
        self.time = 0
        
        
    
class KBGraph:
    
    def __init__(self):
        pass


class NaiveKnowledgeBase(KnowledgeBase):

    def learn(self, config):
        pass

    def makeGraph(self, array):
        return KBGraph() 
