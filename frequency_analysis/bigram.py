from nltk import word_tokenize
from nltk.util import ngrams


text = ['cant railway station', 'citadel hotel', 'police stn']
for line in text:
    token = nltk.word_tokenize(line)
    bigram = list(ngrams(token, 2))
