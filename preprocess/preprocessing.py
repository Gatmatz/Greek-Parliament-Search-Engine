import string
from greek_stemmer import GreekStemmer
import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)  # NFD = Normalization Form Canonical Decomposition,
                   # one of four Unicode normalization forms.
                   if unicodedata.category(c) != 'Mn')  # The character category "Mn" stands for Nonspacing_Mark


# Basic function that removes the punctuation, make the words lowercase,
# removes the one-letter words, removes the stopwords
# and performs STEMMing to the words
def preprocess_text(speech):
    tokens = speech.split()
    filtered = []
    stemmer = GreekStemmer()
    for token in tokens:
        # Remove punctuation and make words lowercase
        cleaned = strip_accents(token.lower().translate(str.maketrans('', '', string.punctuation)))
        # STEM the word
        cleaned = stemmer.stem(cleaned.upper()).lower()
        # Check if the cleaned word is not a one-letter word and not in stopwords
        if len(cleaned) > 2 and cleaned not in stopwords:
            # Αdd it to the final list
            filtered.append(cleaned.lower())
    return ' '.join(filtered)


# Read the stopwords and create a list of them
with open('../data/processed_stopwords-el.txt', 'r') as file:
    stopwords = set(file.read().splitlines())
