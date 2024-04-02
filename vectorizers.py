from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

class TfidfVectorizerCustom:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=10000)

    def vectorize(self, texts):
        return self.vectorizer.fit_transform(texts)

class Word2VecVectorizer:
    def vectorize(self, texts):
        sentences = [word_tokenize(text) for text in texts]
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        return model
