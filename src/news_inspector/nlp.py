import nltk

class DefaultTextProcessor:
    
    def process(self, text):
        return text

def getKeywords(text):
    resp = []
    for sentence in nltk.tokenize.sent_tokenize(text):       
       sentence = nltk.pos_tag(nltk.word_tokenize(sentence.lower()))
       print("\n"+sentence)
       resp.append(sentence)
    return resp
