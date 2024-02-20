import pandas as pd


def fetch_speech(speech_id):
    """
    The fetch_speech is used by the web-app to fetch the selected by the user speech.
        - The function accepts the speech_id and then reads the initial dataset with the speeches (without preprocess).
        - The speech with the given id is returned.
    """
    file_path = '../data/Greek_Parliament_Proceedings_1989_2020.csv'
    df = pd.read_csv(file_path)
    # Check if the row index is within the range of the DataFrame
    if speech_id >= len(df):
        return None

    result_value = df.loc[df['ID'] == speech_id]
    return result_value
