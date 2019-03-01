from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

import news_inspector.nlp as nlp
from news_inspector.core import Trainable

class KnowledgeBase(Trainable):
    
    nodeids = {}
    nodenames = {}
    repodir = None
    n = 0

    @abstractmethod
    def makeGraph(self, array):
        pass    

    def loadNode(self, nodename, params=None): 
        filename = self.repodir+"/"+nodename
        if not os.path.isfile(filename):
            raise Exception("Fatal error. Training configuration file '"+filename+"' not found.")
    
        tree = ET.parse(filename)
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
    
    def findByName(self, name):
        try:
            return self.nodeids[self.nodenames[name]] 
        except:
            return None
   
    def addNode(self, node):
        if not node.name in self.nodenames:
            node.id = self.n
            node.save(self.repodir)
            self.nodenames[node.name] = self.n
            self.nodeids[self.n] = node

            self.n = self.n + 1
     
    def addRelation(self, node, targets):
  
        for target in targets:
            if node != target:
                node.updateArc(target) 
        node.save(self.repodir)

    def addClique(self, nodes):
        for node in nodes:
            if self.findByName(node.name) == None: self.addNode(node)
        for node in nodes:
            self.addRelation(node, nodes)
        
class Node(ABC):
    
    id = None
    name = None
    visited = False 
    arcs = {} 
    tmp = {}

    @abstractmethod        
    def __init__(self, name, attribs=None):    
        pass

    @abstractmethod    
    def updateArc(self, node): 
        pass
    
    @abstractmethod    
    def save(self, repodir):    
        pass    
    
    def traverseDFS(self):
        self.visited = True          
        for arc in arcs:            
            if not arc.target.visited:
                arc.target.traverse()
        
    def traverseBFS(self):
        acum = []
        acum.append(self)
        while len(acum) > 0:
            
            next = acum.pop()
            for arc in next.arcs:
                if not arc.target.visited: acum.append(arc.target)
                    
            next.visited = True             
    
class Arc(ABC):

    def __init__(self, node, attribs=None):
        pass
    
    @abstractmethod    
    def update(attribs=None):    
        pass           
    

class SimpleNode(Node):   
    
    def __init__(self, name, attribs=None):            
        self.name = name
   
    def updateArc(self, node):    
        try:
            self.arcs[node.id].update()
        except:
            self.arcs[node.id] = WeightedArc(node)

    def save(self, repodir):    
        node = ET.Element('node')  
        
        #node.set('id',self.id)  
        #items = ET.SubElement(node, 'items')  

        mydata = ET.tostring(data)  
        myfile = open(repodir+"/"+self.name+".xml", "w")  
        myfile.write(mydata)  
    
    
class WeightedArc(Arc):

    def __init__(self, node, attribs=None):
        self.target = node
        if attribs is not None:
            self.weight = float(attribs['weight'])
    
    def update():
        self.weight = self.weight + 1
        
        
class KBGraph:
    
    def __init__(self):
        pass


class NaiveKnowledgeBase(KnowledgeBase):

    def addNaiveClique(self, names):
        self.addClique([SimpleNode(name) for name in names])
            
    
    def learn(self, config):
        texts = config.getTexts()

        self.repodir = "data/kbrepo"
        for text in texts:
            for sentence in nlp.getSentences(text):
                #print(sentence)
                self.addNaiveClique(nlp.getWords(sentence))
        #print(len(self.nodenames))
    
    def findRelated(self, name, level=1):
        #print(len(self.nodenames))
        return self.findByName(name).arcs
            
    def makeGraph(self, array):
        return KBGraph() 
    

        
