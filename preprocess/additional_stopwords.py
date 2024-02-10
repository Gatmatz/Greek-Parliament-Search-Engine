import pandas as pd


def remove_stopwords(speech):
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
processed_path = '../data/processed_scratch.csv'
dataset = pd.read_csv(processed_path)
# dataset.to_csv(dataset_path, index=True, index_label='ID')

# Read the stopwords and create a list of them
with open('../data/processed_stopwords-el.txt', 'r') as file:
    stopwords = set(file.read().splitlines())

# Perform the preprocess and save the dataset to processed.csv
dataset['speech'] = dataset['speech'].apply(remove_stopwords)
dataset.dropna(subset=['speech', 'member_name'], inplace=True)
dataset.to_csv(processed_path, index=False)
