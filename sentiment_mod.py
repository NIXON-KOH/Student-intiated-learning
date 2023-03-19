from nltk.tokenize import word_tokenize
import pickle
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
       self.classifiers = classifiers
    
    def classify(self, features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self,features):
        votes = []
        for c in self.classifiers:
            v = c.classify(features)
            votes.append(v)
            
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

word_features = open("pickled algos/word_features.pickle","rb")
word_feature = pickle.load(word_features)
word_features.close()

def find(document):
    words = word_tokenize(document)
    features = {}
    for w in word_feature:
        features[w] = (w in words)
    return features


Featuresets = open("pickled algos/featureshufflesets.pickle",'rb')
featuresets = pickle.load(Featuresets)
Featuresets.close()

testing = featuresets[10000:]
training = featuresets[:10000]

Naivebayes_f = open("pickled algos/Naivebayes.pickle","rb")
naivebayes = pickle.load(Naivebayes_f)
Naivebayes_f.close()

BernoulliNB_f = open("pickled algos/BernoulliNB.pickle","rb")
bernoulliNB = pickle.load(BernoulliNB_f)
BernoulliNB_f.close()

LinearSVC_f = open("pickled algos/LinearSVC.pickle","rb")
linearSVC = pickle.load(LinearSVC_f)
LinearSVC_f.close()

MultinomialNB_f = open("pickled algos/MUltinomialNB.pickle","rb")
mulitnomialNB = pickle.load(MultinomialNB_f)
MultinomialNB_f.close()

SGD_f= open("pickled algos/SGD.pickle","rb")
sGD = pickle.load(SGD_f)
SGD_f.close()

NuSVC_f = open("pickled algos/NuSVC.pickle","rb")
nuSVC = pickle.load(NuSVC_f)
NuSVC_f.close()

SVC_f = open("pickled algos/SVC.pickle","rb")
sVC = pickle.load(SVC_f)
SGD_f.close()


voted_classifier = VoteClassifier(bernoulliNB,linearSVC,naivebayes,mulitnomialNB,nuSVC,sGD,sVC)

def sentiment(text):
    feats = find(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
