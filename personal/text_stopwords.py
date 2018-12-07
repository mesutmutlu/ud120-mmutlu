from nltk.corpus import stopwords
import nltk

#nltk.download("stopwords")

sw = stopwords.words("english")

print len(sw)

print sw[12]