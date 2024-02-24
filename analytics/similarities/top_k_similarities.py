import pickle
import os


def fetch_top_k(k):
    """
    The fetch_top_k function accepts a number k and returns the top-k pairs of members with the biggest similarity.
        - The function reads the aggregation_file and the pairwise similarity matrix and creates an array containing the
          pairs with their similarity.
        - For the top-k computation the array is sorted by the similarity value and top-k are kept and returned.
    """
    # Ask for the k parameter
    k = int(k)
    if k < 0:
        k = -k
    elif k == 0:
        k = 10
    # Initialize the array with the top-k pairs
    top_k_pairs = []

    # Build the correct path for the previously computed data files
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Specify the relative path to the 'pickle_matrices' directory
    pickle_matrices_path = os.path.join(current_directory, 'pickle_matrices')

    # Construct the absolute paths for each pickle file
    aggregation_file = os.path.join(pickle_matrices_path, 'aggregation.pkl')
    similarity_file = os.path.join(pickle_matrices_path, 'similarity_matrix.pkl')

    # Open the previously computed matrices and variables
    with open(aggregation_file, 'rb') as file:
        aggregation = pickle.load(file)
    with open(similarity_file, 'rb') as file:
        similarity_matrix = pickle.load(file)

    # Append each unique pair to an array including the similarity score and the members of the pair
    for i in range(len(similarity_matrix)):
        for j in range(i + 1, len(similarity_matrix)):
            top_k_pairs.append(
                ((aggregation['member_name'][i], aggregation['member_name'][j]), similarity_matrix[i][j]))

    # Sort the pairs by similarity
    top_k_pairs = sorted(top_k_pairs, key=lambda x: x[1], reverse=True)[:k]

    return top_k_pairs


def write_to_file():
    """
    Auxiliary function that fetches the top 100 pairs and writes them to a .txt file
    for manual inspection.
    """
    k = 100
    top_k = fetch_top_k(k)
    # Open a file in write mode
    with open(f'top_pairs_{k}.txt', 'w') as f:
        # Iterate over the top k pairs and write each pair to the file
        for pair in top_k:
            f.write(f"{pair[0][0]} - {pair[0][1]}: {pair[1]}\n")