import nltk
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from sklearn.feature_extraction import stop_words
#from nltk.corpus import stopwords

class DefaultTextProcessor:
    
    def process(self, text):
        return text

def getKeywords(text):
    resp = []
    for sentence in sent_tokenize(text):
       tokenizer = RegexpTokenizer(r'[a-z]+')
       sentence = sentence.lower()        
       #tokens = word_tokenize(sentence)
       tokens = tokenizer.tokenize(sentence)  
       print(tokens) 
       #words = [w for w in tokens if not w in stopwords.words('english')]
       words = [w for w in tokens if not w in stop_words.ENGLISH_STOP_WORDS]

       sentence = nltk.pos_tag(words)
       resp.append(sentence)
    return resp
