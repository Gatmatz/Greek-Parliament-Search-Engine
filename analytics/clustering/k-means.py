import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import time
import json

# Διάβασε το αρχείο με τις μειωμένες διαστάσεις
df = pd.read_csv('../LSI/results/lsi_transformation_100.csv')

# Καταγραφή της αρχής της εκτέλεσης
start_time = time.time()

# Σπάσε τη συμβολοσειρά σε λίστα διαστάσεων
df['Topics'] = df['Topics'].str.replace('[','').str.replace(']','').str.split()

# Μετατροπή των στοιχείων της λίστας σε δεκαδικούς αριθμούς
df['Topics'] = df['Topics'].apply(lambda x: [float(i) for i in x])

# Μετατροπή της στήλης "Topics" από λίστα σε στήλες διαστάσεων
df_topics = pd.DataFrame(df['Topics'].tolist(), columns=[f'Topic_{i}' for i in range(100)], index=df.index)

# Ενώνουμε τα δεδομένα
df = pd.concat([df, df_topics], axis=1)

# Επιλογή των στηλών που περιέχουν τις μειωμένες διαστάσεις
X = df[df_topics.columns]

start_time_cluster = time.time()
# Εφαρμογή του αλγορίθμου k-Means
num_clusters = 100
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=300)
df['Cluster'] = kmeans.fit_predict(X)
end_time_cluster = time.time()
print(f"Ο χρόνος εκτέλεσης του clustering είναι: {end_time_cluster-start_time_cluster} δευτερόλεπτα")


start_time_silhouette = time.time()
# Υπολογισμός του Silhouette Score
silhouette_avg = silhouette_score(X, df['Cluster'], metric='cosine')
print(f"Το Silhouette Score είναι: {silhouette_avg}")
end_time_silhouette = time.time()
print(f"Ο χρόνος εκτέλεσης του silhouette είναι: {end_time_silhouette-start_time_silhouette} δευτερόλεπτα")

end_time = time.time()

results = {}
start_time_write = time.time()
unique_clusters = df['Cluster'].nunique()
for cluster_id in range(unique_clusters):
    indices = df[df['Cluster'] == cluster_id]['ID'].tolist()
    cluster_info = {f'Cluster {cluster_id}': {'SpeechId': indices}}
    results.update(cluster_info)

# Αναπροσαρμογή για την εμφάνιση των IDs δίπλα-δίπλα
for cluster_id, cluster_info in results.items():
    cluster_info['SpeechId'] = ', '.join(map(str, cluster_info['SpeechId']))

# Αποθήκευση σε JSON αρχείο
output_file_path = 'output.json'
with open(output_file_path, 'w') as json_file:
    json.dump(results, json_file, indent=2)
end_time_write = time.time()
print(f"Ο χρόνος εκτέλεσης του write είναι: {end_time_write-start_time_write} δευτερόλεπτα")


# Εκτύπωση του χρόνου εκτέλεσης
execution_time = end_time - start_time
print(f"Ο χρόνος εκτέλεσης του προγράμματος είναι: {execution_time} δευτερόλεπτα")
print(f"Τα αποτελέσματα αποθηκεύτηκαν στο αρχείο: {output_file_path}")
