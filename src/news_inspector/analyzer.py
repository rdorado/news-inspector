from text_analyzer import Analyzer
import pymysql
import pickle
import requests
import datetime
import re
import numpy as np

def getFeatures(csr, features_index):
   start = 0
   resp = []
   for i, end in enumerate(csr.indptr[1:]):
      for j, val in zip(csr.indices[start:end], csr.data[start:end]):
          #arr[i,j] = val
          resp.append(features_index[j])
      start = end
   return resp



'''
model1 = CRFNamedEntityExtractor()
model1.train(saveto="myfile", train_texts=["file1", "file2"], fature_set="file")


model2 = N1KnowledgeMap()
model2.train(saveto="myfile", )

//Train
//extractor.train
maker = ModelMaker(algorithm="");
train_model


//Classify

pol_classifier = load_model("pol-classifier.model")
polarity = pol_classifier.classify(txt)

ncat1_classifier = load_model("newscat-classifier.model")
cat1 = ncat1_classifier.classify(txt)


//Extract
ne_params = {};
ne_extractor = load_model("my-model.model");
namedEntities = extractor.extract(txt, ne_params);

fw_params = {};
fw_extractor = load_model("fw-model.model");
functionWords = fw_extractor.extract(txt, fw_params)

knowledge_base = load_model("knowledge-base.model");
graph = knowledge_base.tomap(namedEntities, functionWords);



#TODO: create a connectio class with this info
connection = pymysql.connect(host='127.0.0.1',
                             user='muuddbuser',
                             password='Y!!mqL2aDwV57RP&&9',
                             db='muuddb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

X_docs = []
scraps = []
with connection.cursor() as cursor:
        sql = "select * from scrap as a where a.id_scrap = (select id_scrap from scrap as b where a.id_source = b.id_source order by date_scrapped desc limit 1)"
        cursor.execute(sql)
        scraps = cursor.fetchall() 


#TODO:
# Add rules to the db for each one of the sources/sites
rules =  [{'tag':'div', 'attrs':{'class':'entry-content'}},  {'tag':'h4', 'attrs':{}}]
for scrap in scraps:
   analyzer = Analyzer(scrap['raw_text'])
   doc = ""
   for rule in rules:
      doc += analyzer.getTextAsSingleDoc(rule)
   X_docs.append(doc)

#targets = ["positive","negative","neutral","both"]
targets = ["positive","negative"]
count_vect = pickle.load( open( "../../output/vectorizer_2c.pkl", "rb" ) )
features_index = {indx:wrd for (wrd, indx) in count_vect.vocabulary_.items()}
clf = pickle.load( open( "../../output/clf_2c.pkl", "rb" ) )
predicted = clf.predict(count_vect.transform(X_docs))

i = 0
for scrap in scraps:
   with connection.cursor() as cursor:
      sql = "UPDATE scrap SET polarity = "+str(targets.index(predicted[i]))+" WHERE id_scrap = "+str(scrap['id_scrap'])
      cursor.execute(sql)
   i+=0   
   connection.commit()




'''


