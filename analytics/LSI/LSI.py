import pandas as pd
import os
from gensim import corpora, models
from gensim.parsing.preprocessing import strip_tags, strip_numeric, strip_short, preprocess_string
import pickle

# Set custom filters for GENSIM preprocessing
# The preprocessing involves tokenization, removing the tokens that contain numbers,
# and remove the tokens with less than 3 characters.
CUSTOM_FILTERS = [strip_tags, strip_numeric, strip_short]


def tokenize(speech):
    return preprocess_string(speech, CUSTOM_FILTERS)


# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
dataset = pd.read_csv(dataset_path)
speeches = dataset['speech'].astype(str)

processed_corpus = speeches.apply(tokenize)

dictionary_path = "storage/dictionary.dict"
if os.path.exists(dictionary_path):
    dictionary = corpora.Dictionary.load(dictionary_path)
else:
    dictionary = corpora.Dictionary(processed_corpus)
    dictionary.save(dictionary_path)


bow_corpus_path = "storage/bow_corpus.pkl"
if os.path.exists(bow_corpus_path):
    with open(bow_corpus_path, "rb") as file:
        bow_corpus = pickle.load(file)
else:
    bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
    with open(bow_corpus_path, "wb") as file:
        pickle.dump(bow_corpus, file)


tfidf_path = "storage/tfidf_model"
if os.path.exists(tfidf_path):
    tfidf = models.TfidfModel.load(tfidf_path)
else:
    tfidf = models.TfidfModel(bow_corpus, smartirs='npu')
    tfidf.save(tfidf_path)

corpus_tfidf_path = "storage/corpus_tfidf.pkl"
if os.path.exists(corpus_tfidf_path):
    with open(corpus_tfidf_path, "rb") as file:
        corpus_tfidf = pickle.load(file)
else:
    corpus_tfidf = tfidf[bow_corpus]
    with open(corpus_tfidf_path, "wb") as file:
        pickle.dump(corpus_tfidf, file)

# Compute Latent Semantic Indexing
lsi = models.LsiModel(corpus_tfidf, num_topics=1000)

# Express each speech to the new dimension of topics
speech_vectors = []
for doc in corpus_tfidf:
    vec_lsi = lsi[doc]
    speech_vectors.append(vec_lsi)

new_vectors = []
for speech_scores in speech_vectors:
    speech_vector = [score for _, score in speech_scores]
    new_vectors.append(speech_vector)

print(new_vectors)
