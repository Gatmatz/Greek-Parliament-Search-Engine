import pandas as pd
from preprocess.preprocessing import preprocess_text

# Read the dataset
dataset_path = '../data/Greek_Parliament_Proceedings_1989_2020.csv'
processed_path = '../data/Processed_Greek_Parliament.csv'
dataset = pd.read_csv(dataset_path)

# Perform the preprocess and save the dataset to processed.csv
dataset['speech'] = dataset['speech'].apply(preprocess_text)
dataset.insert(0, 'ID', range(1, len(dataset) + 1))
dataset.to_csv(processed_path, index=False)
