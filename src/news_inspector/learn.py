import nltk
from nltk.classify import NaiveBayesClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle


with open("../../data/subjclueslen1-HLTEMNLP05-v2.tff", "r") as f:
   lines = f.readlines()

#train_targets = ["positive","negative","neutral","both"]
train_targets = ["positive","negative"]
docs ={cl:[] for cl in train_targets}
for line in lines:
  splits = line.strip().split(" ")
  try:
     wrd = splits[2].replace("word1=","")
     targt = splits[5].replace("priorpolarity=","")
     if wrd not in  docs[targt]: docs[targt].append(wrd) 
  except:
     pass


train_data = [" ".join(docs[target]) for target in train_targets]
count_vect = CountVectorizer()
X_train = count_vect.fit_transform(train_data)
clf = MultinomialNB().fit(X_train, train_targets)
#clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None).fit(X_train, train_targets)

pickle.dump( count_vect , open( '../../output/vectorizer_2c.pkl' , "wb" ) )
pickle.dump( clf , open( '../../output/clf_2c.pkl' , "wb" ) )


