# implementation of TF-IDF
import pandas as pd
import pickle as pkl
import os


# Perform a search in the engine
def search(query):
    return [8, 7, 6, 5, 4, 3, 2, 1, 0]  # Dummy results (will be in this format)


corpus_path = "../engine/corpus.pkl"
if not (os.path.exists(corpus_path)) or not (os.path.getsize(corpus_path) > 0):
    # Read the dataset
    dataset = pd.read_csv('../data/small.csv')

    catalog = [8, 7, 6, 5, 4, 3, 2, 1, 0]  # Dummy catalog (will not be in this format)

    # Write the TF_IDF corpus to the system
    with open('../engine/corpus.pkl', 'wb') as corpus:
        pkl.dump(catalog, corpus)

else:
    with open('../engine/corpus.pkl', 'rb') as corpus:
        tfidf_matrix = pkl.load(corpus)
