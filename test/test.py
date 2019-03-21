from news_inspector.core import train_model
from news_inspector.core import load_model
from news_inspector import nlp

from news_inspector.classifiers import GenericClassifier
from news_inspector.retrieval import GenericRetriever
from news_inspector.knowledge_base import NaiveKnowledgeBase

'''
import sys
from muud.database import Source, News

articles = News.findAll();
with open("docs.txt","w") as f:
    for article in articles:
        f.write(article.text+"\n")


sys.exit()
'''

'''
import sys
import xml.etree.ElementTree as ET

confdoc = ET.Element('document')
with open("ner_dataset.csv", "r") as infile:
   for line in infile.readlines():
      if line.startswith("Sentence: "):
         doc = ET.SubElement(confdoc, "sentence")
      splits = line.split(",")
      wrd = ET.SubElement(doc, "word")
      wrd.text = splits[-3].strip()
      wrd.set("pos", splits[-2].strip())
      wrd.set("tag", splits[-1].strip())
      #doc.text = ",".join(splits[-3:]) if doc.text==None else doc.text+",".join(splits[-3:])        

mydata = ET.tostring(confdoc)  
myfile = open("ner_dataset.xml", "wb")  
myfile.write(mydata) 

       
sys.exit()
'''

text = """
Police vehicles and ambulances descended on Lansdowne Centre Friday after a morning shooting.
BC Emergency Health Services spokesperson Shannon Miller said they received a call at 7:33 a.m., and paramedics arrived on scene by 7:44 a.m.
They found one male victim suffering from gunshot wounds, who was transported to hospital in serious condition.
An area outside the Liquor Depot was behind police tape while Mounties investigated. At least eight police vehicles were on scene, and officers were also present at Lansdowne Station.
Mounties cordoned off a section of the parking lot beginning at HomeSense and extending to the north end of the mall. By 3 p.m., the scene was clear and the parking lot fully re-opened.
“We appreciate that this may cause some inconvenience during the holiday season and ask for your continued patience,” said Sgt. Kyle Simpson.
Anyone who witnessed the shooting should call Richmond RCMP at 604-278-1212 and cite file 2018-41056.
"""

train_model(GenericClassifier, "test/polarity-classifier-training-config.xml", "models/polarity-classifier.v0.model");
model = load_model("models/polarity-classifier.v0.model");
result = model.classify(text);
print(result)


train_model(GenericRetriever, "test/location-ir-training-config.xml", "models/location-ir.v0.model");
model = load_model("models/location-ir.v0.model");
locations = model.retrieve(text);
print(locations)

keywords = nlp.getKeywords(text);
print(keywords)

train_model(NaiveKnowledgeBase, "test/naive-knowledgebase-training-config.xml", "models/naive-knowledgebase.v0.model");
model = load_model("models/naive-knowledgebase.v0.model");
print("'"+str(model.findRelated("police"))+"'")
#graph = model.makeGraph(locations + keywords);
#print(graph.listNodesAsStrings())
