from news_inspector.core import train_classifier
from news_inspector.core import load_model

from news_inspector.classifiers import PolarityClassifier


train_classifier(PolarityClassifier, "polarity-classifier-training-config.xml", "polarity-classifier.v0.model");
model = load_model("polarity-classifier.v0.model");
result = model.classify(text);


train_retriever(LocationRetriever, "location-ir-training-config.xml", "location-ir.v0.model");
model = load_model("location-ir.v0.model");
locations = model.retrieve(text);

keywords = nlp.getKeywords(text);


train_knowledgebase(NaiveKBManager, "naive-knowledgebase-training-config.xml", "naive-knowledgebase.v0.model");
model = load_model("naive-knowledgebase.v0.model");
graph = model.adjust(locations + keywords);
