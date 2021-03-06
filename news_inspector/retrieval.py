from abc import abstractmethod
import xml.etree.ElementTree as ET
from sklearn_crfsuite import CRF
import pandas as pd
import numpy as np
import nltk

from news_inspector.core import Trainable

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

'''
def sent2tokens(sent):
    return [token for token, postag, label in sent]


class SentenceGetter(object):
    
    def __init__(self, data):
        self.n_sent = 1
        self.data = data
        self.empty = False
        agg_func = lambda s: [(w, p, t) for w, p, t in zip(s["Word"].values.tolist(),
                                                           s["POS"].values.tolist(),
                                                           s["Tag"].values.tolist())]
        self.grouped = self.data.groupby("Sentence #").apply(agg_func)
        self.sentences = [s for s in self.grouped]
    
    def get_next(self):
        try:
            s = self.grouped["Sentence: {}".format(self.n_sent)]
            self.n_sent += 1
            return s
        except:
            return None
'''


class Retriever(Trainable):
    """
    Retriever abstract class
    """
    
    @abstractmethod
    def retrieve(self, text):
        pass    


class GenericRetriever(Retriever):

     def learn(self, config):  
         texts = config.getTexts()

         sentences = [] 
         for text in texts:
             for sent in ET.fromstring(text).findall('sentence'):
                 stemp = []
                 for wrd in sent.findall('word'):
                     stemp.append([wrd.text, wrd.attrib['pos'], wrd.attrib['tag']])
                 sentences.append(stemp)

         X = [sent2features(s) for s in sentences]
         y = [sent2labels(s) for s in sentences]

         self.clf = CRF(algorithm='lbfgs', c1=10, c2=0.1, max_iterations=100, all_possible_transitions=False)
         self.clf.fit(X, y)


     def retrieve(self, text):
         text = nltk.pos_tag(nltk.word_tokenize(text.lower()))
         X = sent2features(text)
         resp = []
         pred = self.clf.predict([X])[0]
         acum = None
         for i in range(len(pred)):
         
           if pred[i][0] == 'B':
              acum = text[i][0]
           elif pred[i][0] == 'I':
              acum = acum+" "+text[i][0]
           else: 
              if acum != None: resp.append(acum)
              acum = None
           
         return resp


