import pandas as pd
import ast
from collections import Counter

"""
The ner_aggregator.py script aggregates the entities that have been recognised:
The script calculates the number of occurrence of every entities and classify the entity based on its category.
The k-most frequent entities for each tag is calculated and stored in the output/frequent_(k).txt file.

The tags that are supported in the Greek Language are:
PERSON:      People, including fictional.
ORG:         Companies, agencies, institutions, etc.
GPE:         Countries, cities, states.
PRODUCT:     Objects, vehicles, foods, etc. (Not services.)
EVENT:       Named hurricanes, battles, wars, sports events, etc.

(https://stackoverflow.com/questions/76206507/spacy-where-are-terminologies-defined)
"""

crisis = pd.read_csv("output/crisis_final.csv")

# Initialize counters for each entity type
person_counter = Counter()
gpe_counter = Counter()
org_counter = Counter()
event_counter = Counter()
product_counter = Counter()

# Iterate over each row in the DataFrame
for index, row in crisis.iterrows():
    # Parse the named entity recognition tuples from the string representation
    entities = ast.literal_eval(row['entities'])

    # Iterate over each entity tuple
    for entity, entity_type in entities:
        # To capture different aspects of the same entity
        entity = entity.strip('ς').strip('υ')
        # Increment the corresponding counter based on the entity type
        if entity_type == 'PERSON':
            person_counter[entity] += 1
        elif entity_type == 'GPE':
            gpe_counter[entity] += 1
        elif entity_type == 'ORG':
            org_counter[entity] += 1
        elif entity_type == 'EVENT':
            event_counter[entity] += 1
        elif entity_type == 'PRODUCT':
            product_counter[entity] += 1

# Extract the most common entities from each counter
most_common_persons = person_counter.most_common()
most_common_persons = [(person, count) for person, count in most_common_persons if count > 200]

most_common_gpes = gpe_counter.most_common()
most_common_gpes = [(gpe, count) for gpe, count in most_common_gpes if count > 200]

most_common_orgs = org_counter.most_common(100)

most_common_event = event_counter.most_common()
most_common_event = [(event, count) for event, count in most_common_event if count > 10]

most_common_product = product_counter.most_common()
most_common_product = [(product, count) for product, count in most_common_product if count > 10]

with open(f'output/frequent.txt', 'w') as f:
    f.write("Most common PERSON entities:\n")
    for entity, count in most_common_persons:
        f.write(f"{entity}: {count}\n")

    f.write("\nMost common GPE entities:\n")
    for entity, count in most_common_gpes:
        f.write(f"{entity}: {count}\n")

    f.write("\nMost common ORG entities:\n")
    for entity, count in most_common_orgs:
        f.write(f"{entity}: {count}\n")

    f.write("\nMost common EVENT entities:\n")
    for entity, count in most_common_event:
        f.write(f"{entity}: {count}\n")

    f.write("\nMost common PRODUCT entities:\n")
    for entity, count in most_common_product:
        f.write(f"{entity}: {count}\n")

print(f"Entities written to output/frequent.txt")
