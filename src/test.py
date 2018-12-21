from news_inspector.core import train_model
from news_inspector.core import load_model
from news_inspector import nlp

from news_inspector.classifiers import PolarityClassifier


train_model(PolarityClassifier, "polarity-classifier-training-config.xml");
model = load_model("polarity-classifier.v0.model");
result = model.classify(text);


train_model(LocationRetriever, "location-ir-training-config.xml");
model = load_model("location-ir.v0.model");
locations = model.retrieve(text);

keywords = nlp.getKeywords(text);


train_model(NaiveKBManager, "naive-knowledgebase-training-config.xml");
model = load_model("naive-knowledgebase.v0.model");
graph = model.adjust(locations + keywords);
