from news_inspector.train import classifier_trainer
from news_inspector.classifiers import PolarityClassifier


classifier_trainer.train(PolarityClassifier, "polarity-train-config.xml", "polarity-classifier.v1.model");

model = loader.load("polarity-classifier.v1.model");
result = model.classify(text);

