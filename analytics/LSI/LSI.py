import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
speeches = pd.read_csv(dataset_path)

# Initialize the TF-IDF Operation
vectorizer = TfidfVectorizer(sublinear_tf=True)  # Chopping off the terms with big score
tfidf_matrix = vectorizer.fit_transform(speeches['speech'])

# Define the number of topics
num_components = 150

# Create SVD object
lsi = TruncatedSVD(n_components=num_components, random_state=42)

# Fit SVD model on speeches
transformed_tfidf = lsi.fit_transform(tfidf_matrix)

# Define the file name
output_file = f"results/topics_small{num_components}.txt"

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

# Print a speech as an example
transformed_speeches_series = pd.Series()

# Iterate through each speech and transform it
for index, speech in enumerate(speeches['speech']):
    # Transform the speech using TF-IDF
    speech_tfidf = vectorizer.transform([speech])
    # Transform the TF-IDF representation using TruncatedSVD
    speech_transformed = np.array(lsi.transform(speech_tfidf)[0]).flatten()
    # Append the transformed speech to the DataFrame
    transformed_speeches_series.loc[index] = speech_transformed

transformed_speeches_dict = {'ID': speeches['ID'], 'Topics': transformed_speeches_series}
transformed_speeches_df = pd.DataFrame(transformed_speeches_dict)

output_csv_file = 'results/LSI_speeches.csv'
transformed_speeches_df.to_csv(output_csv_file, index=False)

print(f"Transformed speeches saved to {output_csv_file}")
