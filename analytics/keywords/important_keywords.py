import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer

# Read the dataset
dataset_path = '../../data/filtered_speeches_1989_1990.csv'
speeches = pd.read_csv(dataset_path, encoding='utf-8')
speeches = speeches.dropna(subset=['speech'])


def preprocess_text(text):
    return text.split()


speeches['cleaned_speech'] = speeches['speech'].apply(preprocess_text)
speeches['sitting_date'] = pd.to_datetime(speeches['sitting_date'], format='%d-%m-%Y').dt.year.astype(str)

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Store results for MPs and parties per year
mp_year_results = {}
party_year_results = {}

# Iterate through groups (MP and party per year)
for (mp, year), group in speeches.groupby(['member_name', 'sitting_date']):
    speeches_text = [' '.join(doc) for doc in group['cleaned_speech']]

    if not speeches_text:
        continue  # Skip empty documents

    tfidf_matrix = tfidf_vectorizer.fit_transform(speeches_text)
    if tfidf_matrix.shape[1] == 0:
        continue  # Skip if vocabulary is empty

    feature_names = tfidf_vectorizer.get_feature_names_out()
    top_indices = tfidf_matrix.sum(axis=0).argsort()[0, -10:][::-1]  # Select top 10 indices
    top_feature_names = feature_names[top_indices].tolist()  # Convert NumPy array to list
    top_keywords = [fn for fn in top_feature_names]  # Create a new list without encoding or decoding

    mp_year_results.setdefault(mp, {}).update({str(year): top_keywords})

# Iterate through groups (party and year)
for (party, year), group in speeches.groupby(['political_party', 'sitting_date']):
    speeches_text = [' '.join(doc) for doc in group['cleaned_speech']]

    if not speeches_text:
        continue  # Skip empty documents

    tfidf_matrix = tfidf_vectorizer.fit_transform(speeches_text)
    if tfidf_matrix.shape[1] == 0:
        continue  # Skip if vocabulary is empty

    feature_names = tfidf_vectorizer.get_feature_names_out()
    top_indices = tfidf_matrix.sum(axis=0).argsort()[0, -10:][::-1]  # Select top 10 indices
    top_feature_names = feature_names[top_indices].tolist()  # Convert NumPy array to list
    top_keywords = [fn for fn in top_feature_names]  # Create a new list without encoding or decoding

    party_year_results.setdefault(party, {}).update({str(year): top_keywords})

# Combine results
combined_results = {'MPs': mp_year_results, 'Parties': party_year_results}

# Save results to a JSON file
output_file = 'top_keywords_results.json'
with open(output_file, 'w', encoding='utf-8') as f:  # Ensure UTF-8 encoding for JSON file
    json.dump(combined_results, f, indent=4, ensure_ascii=False)  # Set ensure_ascii to False for Unicode characters

print(f"Results saved to {output_file}")
