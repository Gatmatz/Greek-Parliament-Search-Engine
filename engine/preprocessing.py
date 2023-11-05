import string
import pandas as pd
from greek_stemmer import GreekStemmer

# Letter replacement dictionary for accents
dictionary = {
    "έ": "ε",
    "ά": "α",
    "ό": "ο",
    "ή": "η",
    "ύ": "ύ",
    "ί": "ι",
    "ώ": "ω"
}


# Function that removes the accents from a word
def replace_word(word):
    cleared = ""
    for letter in word:
        if letter in dictionary:
            cleared += dictionary[letter]
        else:
            cleared += letter
    return cleared


# Basic function that removes the punctuation, make the words lowercase,
# removes the one-letter words, removes the stopwords
# and performs STEMMing to the words
def preprocess_text(speech):
    tokens = speech.split()
    filtered = []
    stemmer = GreekStemmer()
    for token in tokens:
        # Remove punctuation and make words lowercase
        cleaned = token.lower().translate(str.maketrans('', '', string.punctuation))
        # Check if the cleaned word is not a one-letter word and not in stopwords
        if len(cleaned) > 1 and cleaned not in stopwords:
            # STEM the word and add it to the final list
            cleaned = stemmer.stem(replace_word(cleaned).upper())
            filtered.append(cleaned.lower())
    return ' '.join(filtered)


# Read the dataset
dataset_path = '../data/small.csv'
processed_path = '../data/processed.csv'
dataset = pd.read_csv(dataset_path)

# Read the stopwords and create a list of them
with open('../data/stopwords-el.txt', 'r') as file:
    stopwords = set(file.read().splitlines())

# Perform the preprocess and save the dataset to processed.csv
dataset['speech'] = dataset['speech'].apply(preprocess_text)
dataset.to_csv(processed_path, index=False)
