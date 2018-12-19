from news_inspector.core import train_classifier
from news_inspector.core import load_model

from news_inspector.classifiers import PolarityClassifier


train_classifier(PolarityClassifier, "polarity-train-config.xml", "polarity-classifier.v1.model");
model = load_model("polarity-classifier.v1.model");
result = model.classify(text);

