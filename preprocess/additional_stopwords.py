import pandas as pd

"""
The additional_stopwords.py is an auxiliary function that makes a pass over the set of speeches and removes additional
stopwords without stemming or any other preprocess technique.
The execution of the processor.py is required before the execution of the additional_stopwords.py.
"""


def remove_stopwords(speech):
    """
    The remove_stopwords function accepts a speech and performs an additional preprocessing:
        - Removes all words that have less than 3 letters
        - Removes all stopwords that are in the data/processed_stopwords-el.txt
    """
    tokens = speech.split()
    filtered = []
    for token in tokens:
        # Check if the cleaned word is not a one-letter word and not in stopwords
        if len(token) > 3 and token not in stopwords and not token.isdigit():
            # Αdd it to the final list
            filtered.append(token.lower())
    # Return null if the final speech in empty
    if len(filtered) == 0:
        return None
    return ' '.join(filtered)


# Read the dataset
processed_path = '../data/Processed_Greek_Parliament.csv'
dataset = pd.read_csv(processed_path)
# dataset.to_csv(dataset_path, index=True, index_label='ID')

# Read the stopwords and create a list of them
with open('../data/processed_stopwords-el.txt', 'r') as file:
    stopwords = set(file.read().splitlines())

# Perform the preprocess and save the dataset to processed.csv
dataset['speech'] = dataset['speech'].apply(remove_stopwords)
dataset.dropna(subset=['speech', 'member_name'], inplace=True)
dataset.to_csv(processed_path, index=False)
