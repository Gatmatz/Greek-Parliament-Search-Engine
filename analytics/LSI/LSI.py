import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
"""
The LSI.py script executes Latent Semantic Analysis on the initial speeches dataset:
    - The number of topics is defined in the variable num_components.
    - The LSA is generated by the sklearn library TruncatedSVD.
    - The TF-IDF that is executed before the LSI is using sublinear term frequency to punish stopwords.
      like verbs or non-context words.
    - After the LSA the percentage of total variance explained by the selected components is computed to
      see how much of information is kept from the original dataset.
    - The most similar keywords of each topic along with the % of total variance is saved to topics(num_components).txt.
    - The transformed dataset with each speech expressed in the new dimensions is 
      saved to lsi_transformation_(num_components).csv
"""

# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
speeches = pd.read_csv(dataset_path)

# Initialize the TF-IDF Operation
vectorizer = TfidfVectorizer(sublinear_tf=True)  # Chopping off the terms with big score
tfidf_matrix = vectorizer.fit_transform(speeches['speech'])

# Define the number of topics
num_components = 200

# Create SVD object
lsi = TruncatedSVD(n_components=num_components, random_state=42)

# Fit SVD model on speeches and transform the given speeches
transformed_tfidf = lsi.fit_transform(tfidf_matrix)

# Define the file name
output_file = f"results/topics{num_components}.txt"

# Redirect stdout to the output file
original_stdout = sys.stdout
with open(output_file, "w") as f:
    sys.stdout = f

    # Print the topics with their terms
    terms = vectorizer.get_feature_names_out()

    for index, component in enumerate(lsi.components_):
        zipped = zip(terms, component)
        top_terms_key = sorted(zipped, key=lambda t: t[1], reverse=True)[:5]
        top_terms_list = list(dict(top_terms_key).keys())
        print("Topic " + str(index) + ": ", top_terms_list)

    variance_explained = sum(lsi.explained_variance_ratio_) * 100
    print("Percentage of total variance explained by the selected components: {:.2f}%".format(variance_explained))

# Restore stdout
sys.stdout = original_stdout

# Create a CSV file with the transformed speeches with their ID
# Write the CSV to the disk
output = pd.DataFrame()
output['ID'] = speeches['ID']
output['Topics'] = [vector for vector in transformed_tfidf]
output.to_csv(f'results/lsi_transformation_{num_components}.csv', index=False)
