from abc import ABC, abstractmethod
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from news_inspector.nlp import DefaultTextProcessor
import pickle

class Classifier(ABC):
    
     @abstractmethod
     def classify(self, text):
        pass    

     @abstractmethod
     def learn(self, texts, targets, output, textProcessor = none):
        pass    
    
class PolarityClassifier(Classifier):
    
    def classify(self, text):
        X_test = self.count_vect.transform(text)
        return self.clf.predict(X_test)

    def learn(self, texts, targets, output, textProcessor = none):
        
        if textProcessor == none:
            textProcessor = DefaultTextProcessor() 
        
        train_data = []
        for text in texts:
            train_data.append(textProcessor.process(text))
        
        count_vect = CountVectorizer()
        X_train = self.count_vect.fit_transform(train_data)
        self.clf = MultinomialNB().fit(X_train, targets)

        pickle.dump(self, open( output , "wb" ))
    
    
    
   
