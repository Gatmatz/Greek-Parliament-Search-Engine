import json
import pandas as pd
from time import time
from sklearn.cluster import KMeans, MiniBatchKMeans, BisectingKMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


def perform_lsi(speeches, num_components):
    """
    The perform_lsi function executes Latent Semantic Analysis on the initial speeches dataset:
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

    # Initialize the TF-IDF Operation
    vectorizer = TfidfVectorizer(sublinear_tf=True)  # Chopping off the terms with big score
    tfidf_matrix = vectorizer.fit_transform(speeches['speech'])

    # Define the number of topics
    num_components = num_components

    # Create SVD object
    lsi = TruncatedSVD(n_components=num_components, random_state=42)

    # Fit SVD model on speeches and transform the given speeches
    transformed_tfispeeches = lsi.fit_transform(tfidf_matrix)

    return transformed_tfispeeches


start_time = time()

start_time_pross = time()
# Initialize the dataset path
dataset_path = '../../data/Processed_Greek_Parliament.csv'
# Read the dataset path
speeches = pd.read_csv(dataset_path)

lsi_speeches = perform_lsi(speeches, 100)
end_time_pross = time()
print(f"Ο χρόνος εκτέλεσης του pross είναι: {end_time_pross - start_time_pross} δευτερόλεπτα")

start_time_cluster = time()

# Εφαρμογή του αλγορίθμου k-Means
num_clusters = 100
cluster_method = 'MiniBatchKMeans'

if cluster_method == 'KMeans':
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    speeches['Cluster'] = kmeans.fit_predict(lsi_speeches)
elif cluster_method == 'DBSCAN':
    dbscan = DBSCAN(eps=0.9, min_samples=100, metric='cosine', n_jobs=-1)
    speeches['Cluster'] = dbscan.fit_predict(lsi_speeches)
elif cluster_method == 'MiniBatchKMeans':
    mbkmeans = MiniBatchKMeans(n_clusters=num_clusters, random_state=42)
    speeches['Cluster'] = mbkmeans.fit_predict(lsi_speeches)
elif cluster_method == 'BisectingKMeans':
    bkmeans = BisectingKMeans(n_clusters=num_clusters, random_state=42)
    speeches['Cluster'] = bkmeans.fit_predict(lsi_speeches)
else:
    print(f"Άγνωστη μέθοδος ομαδοποίησης: {cluster_method}")

end_time_cluster = time()
print(f"Ο χρόνος εκτέλεσης του clustering είναι: {end_time_cluster - start_time_cluster} δευτερόλεπτα")

start_time_silhouette = time()
# Υπολογισμός του Silhouette Score
silhouette_avg = silhouette_score(lsi_speeches, speeches['Cluster'], metric='cosine', sample_size=100000)
print(f"Το Silhouette Score είναι: {silhouette_avg}")
end_time_silhouette = time()
print(f"Ο χρόνος εκτέλεσης του silhouette είναι: {end_time_silhouette - start_time_silhouette} δευτερόλεπτα")

end_time = time()

results = {}
start_time_write = time()
unique_clusters = speeches['Cluster'].nunique()
for cluster_id in range(unique_clusters):
    indices = speeches[speeches['Cluster'] == cluster_id]['ID'].tolist()
    num_speeches = len(indices)
    cluster_info = {
        f'Cluster {cluster_id}': {
            'ClusterSize': num_speeches,
            'SpeechId': indices
        }
    }
    print('cluster ', cluster_id, '  size:', len(indices))
    results.update(cluster_info)

# Αναπροσαρμογή για την εμφάνιση των IDs δίπλα-δίπλα
for cluster_id, cluster_info in results.items():
    cluster_info['SpeechId'] = ', '.join(map(str, cluster_info['SpeechId']))

# Αποθήκευση σε JSON αρχείο
output_file_path = 'output.json'
with open(output_file_path, 'w') as json_file:
    json.dump(results, json_file, indent=2)
end_time_write = time()
print(f"Ο χρόνος εκτέλεσης του write είναι: {end_time_write - start_time_write} δευτερόλεπτα")

# Εκτύπωση του χρόνου εκτέλεσης
execution_time = end_time - start_time
print(f"Ο χρόνος εκτέλεσης του προγράμματος είναι: {execution_time} δευτερόλεπτα")
print(f"Τα αποτελέσματα αποθηκεύτηκαν στο αρχείο: {output_file_path}")
