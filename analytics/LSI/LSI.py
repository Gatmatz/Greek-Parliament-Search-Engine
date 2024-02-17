import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
speeches = pd.read_csv(dataset_path)

# Initialize the TF-IDF Operation
vectorizer = TfidfVectorizer(sublinear_tf=True)    # Chopping off the terms with big score
tfidf_matrix = vectorizer.fit_transform(speeches['speech'])

# Define the number of topics
num_components = 200

# Create SVD object
lsi = TruncatedSVD(n_components=num_components, random_state=42)

# Fit SVD model on speeches
lsi.fit_transform(tfidf_matrix)

# Define the file name
output_file = f"topics{num_components}.txt"

# Redirect stdout to the output file
sys.stdout = open(output_file, "w")

# Print the topics with their terms
terms = vectorizer.get_feature_names_out()

for index, component in enumerate(lsi.components_):
    zipped = zip(terms, component)
    top_terms_key = sorted(zipped, key=lambda t: t[1], reverse=True)[:5]
    top_terms_list = list(dict(top_terms_key).keys())
    print("Topic " + str(index) + ": ", top_terms_list)

variance_explained = sum(lsi.explained_variance_ratio_) * 100
print("Percentage of total variance explained by the selected components: {:.2f}%".format(variance_explained))

# Close the file
sys.stdout.close()
