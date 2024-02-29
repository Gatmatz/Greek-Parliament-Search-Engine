import spacy
import pandas as pd


"""
The NER.py script reads the crisis dataset and performs Named-Entity Recognition on the speeches.
Creates a new dataset that for every speech if an entity is found then it creates a tuple in the form (entity, entity_type)
Saves the entity recognition in the output/entities_crisis.csv
"""

nlp = spacy.load("el_core_news_sm")


def extract_entities(row):
    """
    Function to perform entity recognition on a speech
    """
    doc = nlp(row['speech'])
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Processed ID:", row['ID'])
    return entities


if __name__ == '__main__':
    # Initialize the dataset path
    dataset_path = '../../data/crisis.csv'

    # Read the entire dataset
    data = pd.read_csv(dataset_path)

    print("Finished reading")

    # Apply entity recognition to all speeches
    data['entities'] = data.apply(extract_entities, axis=1)

    # Filter out rows with no entities
    data = data[data['entities'].apply(len) > 0]

    print("Finished processing all speeches.")

    # Write processed data to a CSV file
    data.to_csv('output/entities_crisis.csv', index=False)

    print("Processed data saved to entities_crisis.csv")
