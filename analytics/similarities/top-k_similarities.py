import pickle
import os

# Ask for the k parameter
k = int(input('Give the number of top-k similarities you want: '))
# Initialize the array with the top-k pairs
top_k_pairs = []

# Build the correct path for the previously computed data files
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the relative path to the 'pickle_matrices' directory
pickle_matrices_path = os.path.join(current_directory, 'pickle_matrices')

# Construct the absolute paths for each pickle file
aggregation_file = os.path.join(pickle_matrices_path, 'aggregation.pkl')
tfidf_file = os.path.join(pickle_matrices_path, 'tfidf_matrix.pkl')
similarity_file = os.path.join(pickle_matrices_path, 'similarity_matrix.pkl')

# Open the previously computed matrices and variables
with open(aggregation_file, 'rb') as file:
    aggregation = pickle.load(file)
with open(tfidf_file, 'rb') as file:
    tfidf_matrix = pickle.load(file)
with open(similarity_file, 'rb') as file:
    similarity_matrix = pickle.load(file)

# Append each unique pair to an array including the similarity score and the members of the pair
for i in range(len(similarity_matrix)):
    for j in range(i + 1, len(similarity_matrix)):
        top_k_pairs.append(((aggregation['member_name'][i], aggregation['member_name'][j]), similarity_matrix[i][j]))

# Sort the pairs by similarity
top_k_pairs = sorted(top_k_pairs, key=lambda x: x[1], reverse=True)[:k]

# Display top-k pairs
print(f"Top-{k} Similarity Pairs of Parliament Members:")
for pair, similarity in top_k_pairs:
    print(f"Pair: {pair}, Similarity: {similarity}")
