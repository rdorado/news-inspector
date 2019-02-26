from abc import abstractmethod
import xml.etree.ElementTree as xmlreader

from news_inspector.core import Trainable

class KnowledgeBase(Trainable):
    
    @abstractmethod
    def makeGraph(self, array):
        pass    

    def loadNode(self, nodename, params=None): 
        filename = self.repodir+"/"+nodename
        if not os.path.isfile(filename):
            raise Exception("Fatal error. Training configuration file '"+filename+"' not found.")
    
        tree = xmlreader.parse(filename)
        root = tree.getroot()         
    
        module = root.attrib['module']
        class_name = root.attrib['class']
        clazz = getattr(module, class_name)
        
        node = clazz(root.attrib)
        node.id=int(root.attrib['id'])
        node.name=root.attrib['name']
        
        for doc in root.iter('arc'):
            module = doc.attrib['module']
            class_name = doc.attrib['class']
            clazz = getattr(module, class_name)
            node.addArc(clazz(doc.attrib))
        
        self.nodeids[node.id] = node
        self.nodenames[node.name] = node.id    
    
    
class Node(ABC):
     
    def __init__(self, attribs):    
        self.id = attribs['id']
        self.name = attribs['name']
    
    @abstractmethod    
    def save(repodir):    
        pass    
    
    
    
class Arc(ABC):

    def __init__(self, attribs):
        pass
            
    
class SimpleNode(Node):   
    
    def __init__(self, attribs):    
        self.id = None
        self.name = None
        self.arcs = {}  # 'type_of_rel': [id1, id2] 
   
    def save(repodir):    
        pass
    
    
class WeightedArc(Arc):

    def __init__(self, attribs):
        self.target = int(attribs['target'])
        self.weight = float(attribs['weight'])
        self.time = int(attribs['time'])
        
        
    
class KBGraph:
    
    def __init__(self):
        pass


class NaiveKnowledgeBase(KnowledgeBase):

    def learn(self, config):
        pass

    def makeGraph(self, array):
        return KBGraph() 
    

        
