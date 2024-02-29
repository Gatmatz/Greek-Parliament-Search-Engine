import pandas as pd

"""
The crisis_generator.py script creates a subset of the original dataset that starts from
    - September 2, 2009: The Prime Minister K. Karamanlis announces early elections.
and ends on:
    - August 20, 2018: The third memorandum expires and Greece exits the memorandum supervision.
The new dataset is saved to data/crisis.csv
"""

# Read the CSV file
speeches = pd.read_csv("../../data/Greek_Parliament_Proceedings_1989_2020.csv")

# Convert the date column to datetime format
speeches['sitting_date'] = pd.to_datetime(speeches['sitting_date'], format='%d/%m/%Y')

# Filter speeches between September 2, 2009, and August 20, 2018
crisis_df = speeches[(speeches['sitting_date'] >= '2009-09-02') & (speeches['sitting_date'] <= '2018-08-20')]

# Save the filtered DataFrame to a new CSV file
crisis_df.to_csv("../../data/crisis.csv", index=False)

