import string
from greek_stemmer import GreekStemmer
import unicodedata
import spacy

"""
The preprocessing.py script contains the necessary functions for the preprocessing pipeline.
"""

def strip_accents(s):
    """
    Function that takes a string (word) and strips any punctuation.
    Removes any ancient or modern greek punctuation symbol.
    Based on: https://github.com/hb20007/hands-on-nltk-tutorial/blob/main/7-1-NLTK-with-the-Greek-Script.ipynb
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)  # NFD = Normalization Form Canonical Decomposition,
                   # one of four Unicode normalization forms.
                   if unicodedata.category(c) != 'Mn')  # The character category "Mn" stands for Nonspacing_Mark


def use_pos(token):
    """
    Additional function that returns True if the given word is a verb.
    Used for removing the verbs for the dataset.
    """
    token_pos = [word.pos_ for word in nlp(token)]
    if token_pos == 'VERB':
        return True
    else:
        return False


def preprocess_text(speech):
    """
    Basic function that removes the punctuation, make the words lowercase,
    Removes the three-letter words, removes the stopwords
    and performs STEMMing to the words
    """
    tokens = speech.split()
    filtered = []
    stemmer = GreekStemmer()
    for token in tokens:
        verb_flag = use_pos(token)
        # Remove punctuation and make words lowercase
        cleaned = strip_accents(token.lower().translate(str.maketrans('', '', string.punctuation)))
        # STEM the word
        cleaned = stemmer.stem(cleaned.upper()).lower()
        # Check if the cleaned word is not a very small word and not in stopwords and is not a number
        if len(cleaned) > 3 and cleaned not in stopwords and not cleaned.isdigit() and verb_flag is False:
            # Αdd it to the final list
            filtered.append(cleaned.lower())
    # Return null if the final speech in empty
    if len(filtered) == 0:
        return None
    return ' '.join(filtered)


# Read the stopwords and create a list of them
with open('../data/processed_stopwords-el.txt', 'r') as file:
    stopwords = set(file.read().splitlines())

nlp = spacy.load("el_core_news_sm")
