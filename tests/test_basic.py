'''
from news_inspector.core import train_model
from news_inspector.core import load_model
from news_inspector import nlp

from news_inspector.classifiers import GenericClassifier
from news_inspector.retrieval import GenericRetriever
from news_inspector.knowledge_base import NaiveKnowledgeBase


text = """
Police vehicles and ambulances descended on Lansdowne Centre Friday after a morning shooting.
BC Emergency Health Services spokesperson Shannon Miller said they received a call at 7:33 a.m., and paramedics arrived on scene by 7:44 a.m.
They found one male victim suffering from gunshot wounds, who was transported to hospital in serious condition.
An area outside the Liquor Depot was behind police tape while Mounties investigated. At least eight police vehicles were on scene, and officers were also present at Lansdowne Station.
Mounties cordoned off a section of the parking lot beginning at HomeSense and extending to the north end of the mall. By 3 p.m., the scene was clear and the parking lot fully re-opened.
“We appreciate that this may cause some inconvenience during the holiday season and ask for your continued patience,” said Sgt. Kyle Simpson.
Anyone who witnessed the shooting should call Richmond RCMP at 604-278-1212 and cite file 2018-41056.
"""

train_model(GenericClassifier, "polarity-classifier-training-config.xml", "polarity-classifier.v0.model");
model = load_model("polarity-classifier.v0.model");
result = model.classify(text);
print(result)


#train_model(GenericRetriever, "location-ir-training-config.xml", "location-ir.v0.model");
model = load_model("location-ir.v0.model");
locations = model.retrieve(text);
print(locations)

keywords = nlp.getKeywords(text);
print(keywords)

train_model(NaiveKnowledgeBase, "naive-knowledgebase-training-config.xml", "naive-knowledgebase.v0.model");
model = load_model("naive-knowledgebase.v0.model");
print("'"+str(model.findRelated("bbb"))+"'")
#graph = model.makeGraph(locations + keywords);
#print(graph.listNodesAsStrings())
'''
