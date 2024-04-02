import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.alpha_numeric_re = re.compile('[^a-zA-Z ]+')

    def preprocess_text(self, text):
        clean_text = self.alpha_numeric_re.sub('', text.lower())
        words = word_tokenize(clean_text)
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)
