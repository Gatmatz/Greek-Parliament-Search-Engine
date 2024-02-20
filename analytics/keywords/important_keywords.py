import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer

"""
The important_keywords.py script generates a JSON file that contains:
    1)For every member of the parliament and for every year the most important keywords using TF-IDF scoring.
    2)For every party of the parliament and for every year the most importa keywords using again TF-IDF scoring.
The JSON file is saved to top_keywords_results.json
"""

# Read the dataset
dataset_path = '../../data/Processed_Greek_Parliament.csv'
speeches = pd.read_csv(dataset_path, encoding='utf-8')
speeches = speeches.dropna(subset=['speech'])


def preprocess_text(text):
    return text.split()


speeches['cleaned_speech'] = speeches['speech'].apply(preprocess_text)
speeches['sitting_date'] = pd.to_datetime(speeches['sitting_date'], format='%d/%m/%Y').dt.year.astype(str)


# Function to calculate TF-IDF with TF normalization
def tfidf_with_tf_normalization(corpus):
    tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True)
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    return tfidf_matrix, tfidf_vectorizer.get_feature_names_out(), tfidf_vectorizer.idf_


# Store results for MPs and parties per year
mp_year_results = {}
party_year_results = {}

# Iterate through groups (MP and party per year)
for (mp, year), group in speeches.groupby(['member_name', 'sitting_date']):
    speeches_text = [' '.join(doc) for doc in group['cleaned_speech']]

    if not speeches_text:
        continue  # Skip empty documents

    tfidf_matrix, feature_names, idf_values = tfidf_with_tf_normalization(speeches_text)

    if tfidf_matrix.shape[1] == 0:
        continue  # Skip if vocabulary is empty

    # Calculate the sum of TF-IDF values for each feature and divide by IDF if we want to use the normalized form
    normalized = False
    if normalized:
        sum_tfidf_by_idf = (tfidf_matrix.sum(axis=0) / idf_values).tolist()[0]
    else:
        sum_tfidf_by_idf = (tfidf_matrix.sum(axis=0)).tolist()[0]

    top_indices = sorted(range(len(sum_tfidf_by_idf)), key=lambda i: sum_tfidf_by_idf[i], reverse=True)[:10]
    top_feature_names = [feature_names[i] for i in top_indices]

    mp_year_results.setdefault(mp, {}).update({str(year): top_feature_names})

# Iterate through groups (party and year)
for (party, year), group in speeches.groupby(['political_party', 'sitting_date']):
    speeches_text = [' '.join(doc) for doc in group['cleaned_speech']]

    if not speeches_text:
        continue  # Skip empty documents

    tfidf_matrix, feature_names, idf_values = tfidf_with_tf_normalization(speeches_text)

    if tfidf_matrix.shape[1] == 0:
        continue  # Skip if vocabulary is empty

    # Calculate the sum of TF-IDF values for each feature and divide by IDF
    sum_tfidf_by_idf = (tfidf_matrix.sum(axis=0) / idf_values).tolist()[0]

    top_indices = sorted(range(len(sum_tfidf_by_idf)), key=lambda i: sum_tfidf_by_idf[i], reverse=True)[:10]
    top_feature_names = [feature_names[i] for i in top_indices]

    party_year_results.setdefault(party, {}).update({str(year): top_feature_names})

# Combine results
combined_results = {'MPs': mp_year_results, 'Parties': party_year_results}

# Save results to a JSON file
output_file = 'top_keywords_results.json'
with open(output_file, 'w', encoding='utf-8') as f:  # Ensure UTF-8 encoding for JSON file
    json.dump(combined_results, f, indent=4, ensure_ascii=False)  # Set ensure_ascii to False for Unicode characters

print(f"Results saved to {output_file}")
