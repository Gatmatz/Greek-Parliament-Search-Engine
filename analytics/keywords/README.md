# Important Keywords

The aim of this question is to identify the most important keywords per MP and per party and how they change over time.

First, there are some data processing steps in which, the Processed_Greek_Parliament.csv file containing the speech texts of members of parliament is loaded, the texts with NaN values are removed and the dates are converted to year format. Each speech is then pre-processed, during which the texts are tokenised.

Two empty dictionary objects, mp_year_results and party_year_results, are then created to store the results of the speeches for MPs and parties by year respectively.

The method for computing the results is common to both themes.

For example, to find the most important keywords per MP, groupby is used which groups the data by member (member_name) and year (sitting_date). Speech texts (speeches_text) are generated from the texts of each group and the function tfidf_with_tf_normalization is called to compute the TF-IDF.

TF-IDF is executed with the help of the sklearn library and more specifically TfidfVectorizer. More specifically, the tfidf_with_tf_normalization function computes the TF-IDF (Term Frequency-Inverse Document Frequency) for a set of texts by normalizing the term frequency (TF normalization). It creates a tfidfVectorizer object and sets the parameter sublinear_tf = True, so that the term frequency is computed as 1 + log(tf). This penalizes words that occur too often and have no context. It applies the TfidfVectorizer to the set of texts and computes the TF-IDF matrix, tfidf_matrix, where each row corresponds to a document and each column corresponds to an attribute (word). It returns the tfidf_matrix, the feature words used tfidf_vectorizer.get_feature_names_out(), and the inverse IDF (Inverse Document Frequency) tfidf_vectorizer.idf_.

<https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html>

After the tfidf_matrix, feature_names, idf_values are calculated, if the user wants to normalize by the IDF of each feature, he sets the variable

_normalized = True._ Otherwise, by default the code is executed without normalization.

By normalization we mean dividing the sum score of each term by the idf of the term to further penalize words with frequent occurrences that have no context (such as verbs).

Finally, we perform a ranking (descending order) based on TF-IDF values and select the top 10 keywords with the highest TF-ID values. These results are stored in mp_year_results and party_year_results respectively.

The overall results are stored in a .json file, top_keywords_results.json, which has the format:

for each MP shown:

- the top 10 keywords by year, and

for each party, the top 10 keywords for each party are shown:

- the 10 most important keywords per year.