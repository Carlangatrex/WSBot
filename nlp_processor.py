import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('spanish'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens

    def get_intent(self, text):
        tokens = self.preprocess_text(text)
        if 'comprar' in tokens and 'juguete' in tokens:
            return 'comprar_juguete'
        elif 'sesion' in tokens and 'intima' in tokens:
            return 'comprar_sesion_intima'
        return 'chat'

    def get_excitement_level(self, text):
        tokens = self.preprocess_text(text)
        excitement_words = ['excitado', 'caliente', 'sexy', 'pasion', 'deseo']
        excitement_level = sum(1 for token in tokens if token in excitement_words)
        return min(excitement_level * 20, 100)  # Scale to 0-100

