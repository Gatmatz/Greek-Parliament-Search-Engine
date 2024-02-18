import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer


# Read the dataset
dataset_path = '../../data/filtered_speeches_1989_1990.csv'
speeches = pd.read_csv(dataset_path, encoding='utf-8')
speeches = speeches.dropna(subset=['speech'])


# Preprocess text
def preprocess_text(text):
    return text.split()


speeches['cleaned_speech'] = speeches['speech'].apply(preprocess_text)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(sublinear_tf=True)
tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(doc) for doc in speeches['cleaned_speech']])

# Δημιουργία του μοντέλου Agglomerative Clustering
model = AgglomerativeClustering(linkage='average')

# Εκπαίδευση του μοντέλου
model.fit(tfidf_matrix.toarray())

# Εκτύπωση των ομάδων που έχουν δημιουργηθεί
print("Ομάδες ομιλιών:")
for i in range(len(speeches)):
    print(f"Ομιλία {i+1} ανήκει στην ομάδα {model.labels_[i]}")