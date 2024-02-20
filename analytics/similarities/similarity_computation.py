import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
The similarity_computation.py script generates the pairwise similarity of each member in the Parliament:
    - Per member the speeches of each member is aggregated to one row separating each word with a space
      creating a new .csv file that is saved to aggregation.pkl using pickle's library.
    - Next a TF-IDF is executed on the newly aggregated speeches using sublinear term frequency and removing terms 
      with max_df over the 80% for punishing stopwords like verbs or non-context words.
    - For the pairwise similarity computation is used the similarity_matrix of sklearn. The pairwise similarity is
      computed and saved to similarity_matrix.pkl.
"""

# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
speeches = pd.read_csv(dataset_path)
speeches = speeches.dropna(subset=['speech'])

aggregation_file = 'pickle_matrices/aggregation.pkl'
tfidf_file = 'pickle_matrices/tfidf_matrix.pkl'
similarity_file = 'pickle_matrices/similarity_matrix.pkl'

# Group the speeches of each member and then merge the speeches into one
aggregation = speeches.groupby('member_name')['speech'].apply(' '.join).reset_index()

# Save Aggregated speeches
with open(aggregation_file, 'wb') as file:
    pickle.dump(aggregation, file)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_df=0.8, sublinear_tf=True)
tfidf_matrix = vectorizer.fit_transform(aggregation['speech'])

# Save TF-IDF matrix
with open(tfidf_file, 'wb') as file:
    pickle.dump(tfidf_matrix, file)

# Calculate the pair-wise cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save similarity matrix
with open(similarity_file, 'wb') as file:
    pickle.dump(similarity_matrix, file)
