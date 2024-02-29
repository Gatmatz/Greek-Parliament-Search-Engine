


# Speech Preprocess

For the most efficient search of terms as well as the most interesting and rewarding knowledge discovery a preprocessing pipeline has been designed for the dataset.

The preprocessing consists of the following steps:

1. tokenization of each speech into word-tokens.
2. removal of punctuation marks (either modern or ancient Greek).
3. Stemming the words to their roots.
4. Filtering words that are considered as stopwords.
5. Filtering words that are less than 3 letters long.
6. Filtering words that are numbers.
7. (Optional) Removing verbs through the tagging process.

For removing punctuation marks (2) a function has been used which has been found in the following repository: <https://github.com/hb20007/hands-on-nltk-tutorial/blob/main/7-1-NLTK-with-the-Greek-Script.ipynb>

For performing Stemming (3) a Greek Stemmer has been used which does not require knowledge of the POS (Part Of Speech) of the word. It requires the word to be converted to uppercase and cannot stem Latin characters. The Stemmer is used in the popular Skroutz application.

<https://github.com/skroutz/greek_stemmer>

The list of stopwords(4) can be found in data/processed_stopwords-el.txt. The stopwords come from two sources:

1. General stopwords of the Greek language (such as articles, pronouns, adverbs) found in the following repository.
2. <https://github.com/stopwords-iso/stopwords-el>.
3. Special stopwords in the context of the speeches of the Parliament (such as "sir", "president", etc.) which were added manually to the list.

**All stopwords go through the stemming phase so that they can be found efficiently (e.g. we avoid persons in pronouns).**

It is possible to remove verbs from the dataset if it is offered for further work. The spaCy library, which supports Greek vocabulary tagging, has been used for verb removal. With the tagging process, the library manages to discover the POS(Part Of Speech) of each word. After finding the POS tag, the verbs can be removed. **The above procedure has not been used in the preprocessing of our dataset, but is given as an option.**

[**https://spacy.io/models/el**](https://spacy.io/models/el)

The scripts referring to preprocessing are located inside the preprocess folder.

The **processor.py** script executes the pipeline, reading the original speech file and applying the preprocess_text function. It then removes the rows that are empty (either in the speech or face field) and writes the newly processed file to memory. Preprocessing the original dataset and storing the processed one amounts to about 11-12 hours.

The script **preprocessing.py** contains the appropriate functions to perform the preprocessing as well as code to read the stopwords and load the Greek model for POS Tagging.

The **additional_stopwords.py** script is utility and allows for the removal of parental stopwords, if desired. The user is prompted to add the desired, new stopwords to the existing list and the script reads the updated list of stopwords. It then removes the new stopwords from the edited speech file and writes the file back to memory.