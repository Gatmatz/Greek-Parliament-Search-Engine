import pandas as pd


def fetch_speech(speech_id):
    file_path = '../data/scratch.csv'
    speech_id = 1
    df = pd.read_csv(file_path)
    # Check if the row index is within the range of the DataFrame
    if speech_id >= len(df):
        return None

    result_value = df.loc[speech_id]
    return result_value
