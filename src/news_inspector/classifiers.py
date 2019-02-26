from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from abc import abstractmethod

from news_inspector.nlp import DefaultTextProcessor
from news_inspector.core import Trainable


class Classifier(Trainable):
    
     @abstractmethod
     def classify(self, text):
        pass    

    
class GenericClassifier(Classifier):
    
    def classify(self, text):
        X_test = self.count_vect.transform([text])
        return self.clf.predict(X_test)

    def learn(self, config, textProcessor = None):
        texts = config.getTexts()
        targets = config.getTargets()
    
        if textProcessor == None:
            textProcessor = DefaultTextProcessor() 
        
        train_data = []
        for text in texts:
            train_data.append(textProcessor.process(text))

        self.count_vect = CountVectorizer()
        X_train = self.count_vect.fit_transform(train_data)
        self.clf = MultinomialNB().fit(X_train, targets)

    
    
    
   
