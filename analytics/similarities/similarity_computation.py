import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
vectorizer = TfidfVectorizer(max_df=0.8)
tfidf_matrix = vectorizer.fit_transform(aggregation['speech'])

# Save TF-IDF matrix
with open(tfidf_file, 'wb') as file:
    pickle.dump(tfidf_matrix, file)

# Calculate the pair-wise cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save similarity matrix
with open(similarity_file, 'wb') as file:
    pickle.dump(similarity_matrix, file)
