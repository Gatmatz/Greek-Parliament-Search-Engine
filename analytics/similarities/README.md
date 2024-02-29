# Pairwise Similarity

The aim of this paper is to detect pairwise similarities between members of parliament. First, we use the TF-IDF technique to express each speech in a feature vector and then compute pairwise cosine similarity for the similarity approximation.

TF-IDF is executed with the help of the sklearn library, specifically TfidfVectorizer. The settings used are:

1. _max_df = 0.8_ so that words with very frequent occurrences are eliminated. Such words are usually verbs which have no context, and are therefore chosen to be removed.
2. _sublinear_tf = True_ so that the term frequency is calculated as 1 + log(tf). In this way, words that occur too often and have no context are penalized again.

The goal is to find similarity of speeches by removing words that all MPs use in their speeches. In this way, we approximate a similarity which reflects (as far as possible) similarity in the actual opinions of the MPs and not in frequently used words without meaning.

First, there is an aggregation of the speeches. Specifically, all the speeches of each MP are gathered into a string (each word is separated by a space). Then, TF-IDF is performed on the aggregated dataset and finally the sklearn similarity_matrix function is used to compute pairwise similarity. The results as well as the intermediate matrices of aggregation and TF-IDF are stored as pickle files in the pickle_matrices folder.

<https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html>

The similarity_computation.py script performs the similarity computation of MPs as described above.

The top_k_similarities.py script is used to present the results in the search engine web app. The script takes a number k and reads the stored clustered speeches and the similarities table and computes the top-k pairs. In the end, it returns them to the web-app for display.

The selection of the number of k is done dynamically and the user can on-the-fly through the web-app adjust the results.

The top-100 pairs can also be viewed manually in the top_pairs_100.txt file.