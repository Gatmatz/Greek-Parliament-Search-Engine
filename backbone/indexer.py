from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh.index import create_in
import csv
import os

schema = Schema(ID=ID(stored=True),
                member_name=STORED,
                sitting_date=STORED,
                parliamentary_period=STORED,
                parliamentary_session=STORED,
                parliamentary_sitting=STORED,
                political_party=STORED,
                speech=TEXT)

# Create an index in a directory
index_directory = "corpus"
if not os.path.exists(index_directory):
    os.makedirs(index_directory)
ix = create_in(index_directory, schema)

# Open the index writer
writer = ix.writer(limitmb=2048)
csv.field_size_limit(1280918)

# Load data from CSV and add documents to the index
csv_file_path = "../data/final_processed.csv"
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        writer.add_document(
            ID=row['ID'],
            member_name=row['member_name'],
            sitting_date=row['sitting_date'],
            parliamentary_period=row['parliamentary_period'],
            parliamentary_session=row['parliamentary_session'],
            parliamentary_sitting=row['parliamentary_sitting'],
            political_party=row['political_party'],
            speech=row['speech'])

# Commit changes and close the writer
writer.commit()

print("Inverted index created successfully.")
