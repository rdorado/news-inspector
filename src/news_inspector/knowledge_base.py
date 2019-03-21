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
    
    def findOrCreate(self, name, clazz):
        node = self.findByName(name)
        if node != None: return node
        node = clazz(name)
        self.addNode(node)
        return node

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
            node.save(self.repodir)
     
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

    def __init__(self, node):
        pass
    
    @abstractmethod    
    def update(self, attribs=None):    
        pass           
    
    @abstractmethod 
    def save(self, ET, node):
        pass
 
class SimpleNode(Node):   
    
    def __init__(self, name, attribs=None):            
        self.name = name
        self.arcs = {}
   
    def updateArc(self, target):    
        try:
            self.arcs[target.id].update()
        except:
            self.arcs[target.id] = WeightedArc(target)

    def save(self, repodir):    
        node = ET.Element('node', name=self.name, id=str(self.id))  
        for arcid, arc in self.arcs.items():
        #node.set('id',self.id)  
           arc.save(node)

        mydata = ET.tostring(node)  
        myfile = open(repodir+"/"+self.name+".xml", "wb")  
        myfile.write(mydata)  
    
    
class WeightedArc(Arc):

    def __init__(self, node):
        self.target = node
        self.weight = 1
        #if attribs is not None:
        #    self.weight = float(attribs['weight'])
    
    def update(self):
        self.weight = self.weight + 1

    def save(self, parent):        
        ET.SubElement(parent, 'arc', target=str(self.target.id), weight=str(self.weight))    
  

class KBGraph:
    
    def __init__(self):
        pass


class NaiveKnowledgeBase(KnowledgeBase):

    def addNaiveClique(self, names):
        
        self.addClique([self.findOrCreate(name, SimpleNode) for name in names])
            
    
    def learn(self, config):
        texts = config.getTexts()

        self.repodir = "kbrepo"
        for text in texts:
            for sentence in nlp.getSentences(text):
                words = nlp.getWords(sentence)

                self.addNaiveClique(words)
        #print(len(self.nodenames))
    
    def findRelated(self, name, level=1):
        #print(len(self.nodenames))
        resp = []
        node = self.findByName(name)
        if node != None: 
            for arcid, arc in self.findByName(name).arcs.items():
                resp.append(arc.target.name)
        return resp
            
    def makeGraph(self, array):
        return KBGraph() 
    

        
