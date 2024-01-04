import pandas as pd

# Read the dataset
dataset_path = 'data/Processed_Greek_Parliament.csv'
processed_path = 'data/filtered_speeches_1989_1990.csv'
speeches = pd.read_csv(dataset_path)

# Drop rows with NaN values in the 'speech' column
speeches = speeches.dropna(subset=['speech'])

# Convert 'sitting_date' column to datetime with dayfirst=True
speeches['sitting_date'] = pd.to_datetime(speeches['sitting_date'], dayfirst=True, errors='coerce')

# Filter speeches based on date range
start_date = pd.to_datetime('1989-01-01')  # Adjusted date format to match dataset
end_date = pd.to_datetime('1991-12-31')   # Adjusted date format to match dataset

filtered_data = speeches[(speeches['sitting_date'] >= start_date) & (speeches['sitting_date'] <= end_date)]

# Format 'sitting_date' column as 'dd-mm-yyyy' before saving
filtered_data['sitting_date'] = filtered_data['sitting_date'].dt.strftime('%d-%m-%Y')

# Save the filtered data to a new CSV file
filtered_data.to_csv(processed_path, index=False)
