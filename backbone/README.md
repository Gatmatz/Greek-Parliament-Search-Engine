# Inverted index

The following part explains the implementation of the search engine backend. In particular, the implementation of the inverted index, the search in it and the retrieval of the original speech from the original (unprocessed) dataset is explained. The implementation scripts are located in the backbone folder.

The implementation of the inverted directory is done using the whoosh library.

The indexer.py script creates the index and stores it in the inverse_index folder. Initially, a schema of the directory is defined in which we define:

1. The ID field of the dataset will be of type ID and in the directory
2. The speech field will be of type TEXT. Therefore a catalog will be built based on this field.
3. The other fields are defined as STORED, therefore they will be kept in the inverted catalog but no index will be made on them.

<https://whoosh.readthedocs.io/en/latest/schema.html>.

The script then creates the appropriate paths and serially reads each speech and adds it to the inverted directory. At the end, by applying the commit call the inverted is built and written to memory. The execution time of the inverted is 30-40 minutes.

Next, the search.py script performs a keyword-based search on the inverted directory. The search is contained in the perform_query function. Specifically, first the inverted is read from memory and loaded. Then the query is passed through the appropriate preprocess. If the word is foreign then it is not tampered with, and if after the preprocess the query is empty (all words were stopwords) then the original query is kept. Finally, the query is searched by TF-IDF and the results are returned. The first 100 results are returned.

Finally, the fetching.py script accepts a speech ID and returns the original speech. During the preprocess, an ID column has been added to the original dataset where it is the primary key of the table. This ID follows each speech either after preprocessing it or any other operation is applied to it. In this way we can at any time find from any operation the original speech from which the results came.

The script loads the original dataset into memory and returns the speech with the given ID for display in the web application. This process takes a long time (1-2 minutes) and therefore is a bottleneck in the search engine.