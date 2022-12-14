from response_preprocessing import log_filter, log_integration, response_data
from sensor_preprocessing import sensor_integration
from voice_preprocessing import voice_integration
from demographic import demographics
import pickle
import pandas as pd

if __name__ == '__main__':

    df = response_data()
    df_sensor = sensor_integration(df)
    df_demo = demographics(df_sensor)
    df_voice = voice_integration(df_demo)
    # print(df_voice.info())

    # pickle로 저장
    pickle_path = 'data.pkl'
    with open(pickle_path, "wb") as file:
        pickle.dump(df_voice, file)

    PATH = 'data.pkl'
    DATASET = pickle.load(open(PATH, mode='rb'))
    print(DATASET.isna().sum())
    print(DATASET.head())
