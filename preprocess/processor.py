import pandas as pd
from preprocess.preprocessing import preprocess_text

"""
The processor.py executes the preprocess pipeline of the dataset.
"""

# Read the dataset
dataset_path = '../data/raw.csv'
processed_path = '../data/processed_scratch.csv'
dataset = pd.read_csv(dataset_path)
# dataset.to_csv(dataset_path, index=True, index_label='ID')

# Perform the preprocess and save the dataset to processed.csv
dataset['speech'] = dataset['speech'].apply(preprocess_text)
dataset.dropna(subset=['speech', 'member_name'], inplace=True)
dataset.to_csv(processed_path, index=False)
