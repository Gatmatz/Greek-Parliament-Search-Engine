# LSI - Topics Selection

In the following part we implement the LSI procedure, in which we use mathematical linear algebra transformations to extract Themes on our speeches and express each speech in terms of the new themes.

The sklearn library, specifically TruncatedSVD, was used to perform the LSI. First, a TF-IDF process is run on the speeches with sublinear term frequency - to _weaken_ the words that appear too much - and then TruncatedSVD is run on the TF-IDF table created.

<https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html>

The number of topics is defined in the num_components variable.

**To evaluate the effectiveness of the LSI, the percentage of total variance explained by the selected topics is used as a metric.

**To express each speech in the new dimensions (topics) it is sufficient to execute the fit_transform command of TruncatedSVD on the TF-IDF table.** Each re-expressed speech is written to the results/lsi_transformation_{num_components}.csv file by adding to each speech the ID of the original speech (foreign key).

The generated topics as well as the 5 most representative words of each topic are written to a file result/topics{num_components}.txt. At the end of the file, the percentage of total variance calculated primarily is also written.

It is observed that as we increase the number of topics, the percentage of total variance increases. But at the same time, the execution time of the LSI process increases dramatically.

The results can be viewed manually from the previously mentioned files and also through the search engine web app.