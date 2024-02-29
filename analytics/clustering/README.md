# Clustering

## Implementation
The aim of this project is to group the speeches so that the speeches of the same group are very similar. Several clustering algorithms such as, K-Means, Bisecting-KMeans, MiniBatch-KMeans, Agglomerative, DBSCAN were tried for clustering the speeches, but not all of them worked as we wanted. Agglomerative, DBSCAN algorithms were impossible to execute on our computers as the dataset used (Processed_Greek_Parliament.csv) is too large and on simple computers it results in program termination due to lack of memory to execute it. Below is the implementation of the remaining algorithms and their evaluation against the Silhouette Score metric for evaluating the clustering quality and execution time.

First, a preprocessing is performed which consists of reading the processed dataset Processed_Greek_Parliament.csv and executing the function perform_lsi which takes as parameters the .csv file and an integer representing the reduced dimensions we want each speech to have, and returns the speeches with reduced dimensions. By default the code is reduced to 100 dimensions.

Next, it is the turn to group the speeches. K-Means, Bisecting-KMeans, MiniBatch-KMeans Algorithms were used for clustering which were tested for different k (k=50, 100, 200, 1000, 10000) as shown in the tables below. In the code there is an if used to select the clustering algorithm we want to run by placing the name of the algorithm in the cluster_method variable.

It is also important to calculate the Silhouette Score to evaluate the quality of the clustering in question. The Silhouette Score takes values from -1 to 1. The closer to 1 the better the clustering is, while the closer to -1 the clustering is not done in the best possible way.

The results are stored in a .json file, clustering_results.json, which

for each cluster displays the number of speeches it contains and their ID (foreign key) so that the user can refer to the speeches if he wants to. At the same time, the IDE screen also displays the runtimes of the lsi, the clustering, the silhouette score and the program as a whole. Still, the silhouette score and the name of the file in which the final results were saved are displayed.

## Results

### Based on Silhouette Score
We note that for the given values of k there is no algorithm that is "perfect", i.e., close enough to 1. However, it is observed that MiniBatch-KMeans with the given k gives better scores than the other two algorithms. This may be due to the fact that it uses mini-batches of data instead of computing the center of clusters for the whole dataset. This speeds up the training as it does not require examining all samples at a time. Still, using mini-batches allows MiniBatchKMeans to be more independent of its original center selection, as it updates the cluster centers in each mini-batch. This can lead to more flexible alternatives. Immediately following MiniBatch-KMeans, better results are obtained by K-Means with very little difference from Bisecting-KMeans. It is also observed that in general, as k increases, the Silhouette Score decreases.

### Based on Running Time
In general, MiniBatch-KMeans runs faster than the other two algorithms. Bisecting-KMeans comes next and the worst in terms of execution time is the classic KMeans. This difference may be due to the fact that MiniBatch-KMeans uses small portions (mini-batches) of the data for training, while the other algorithms examine the entire dataset. This allows parallelization of computations and reduces the runtime on large datasets. Still, Bisecting-KMeans adopts the cluster splitting procedure, which may be more efficient than KMeans in some cases, especially when some clusters are easier to split.

The final conclusion is that the best batching algorithm for this dataset turns out to be MiniBatch-KMeans since it has the best runtime and Silhouette Score compared to the other two algorithms. However, this does not mean that this is always true, but only for the specific dataset with the specific k.