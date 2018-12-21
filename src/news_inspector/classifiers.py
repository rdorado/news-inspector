from abc import ABC, abstractmethod
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from news_inspector.nlp import DefaultTextProcessor
from news_inspector.core import Trainable
import pickle

class Classifier(Trainable):
    
     @abstractmethod
     def classify(self, text):
        pass    


    
class PolarityClassifier(Classifier):
    
    def classify(self, text):
        X_test = self.count_vect.transform(text)
        return self.clf.predict(X_test)

    def learn(self, config, textProcessor = None):
        texts = config.getTexts()
        targets = config.getTargets()
        output = config.getOutputFileName()
         
    
        if textProcessor == None:
            textProcessor = DefaultTextProcessor() 
        
        train_data = []
        for text in texts:
            train_data.append(textProcessor.process(text))
        
        self.count_vect = CountVectorizer()
        X_train = self.count_vect.fit_transform(train_data)
        self.clf = MultinomialNB().fit(X_train, targets)

        pickle.dump(self, open( output , "wb" ))
    
    
    
   
