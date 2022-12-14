import csv
import os
import pandas as pd


def sensor_integration(df):
    # read sensor data
    csv_path = os.path.join("sensor_data.csv")
    df_sensor = pd.read_csv(csv_path)

    sensor_data = []


    for i in range(0, len(df)):
        current_uid = int(df['uid'][i])
        startTime = int(df['startTime'][i] / 1000.0)  # sec

        before = startTime - 60 * 1  # 시작 1분 전
        # print('uid', current_uid)
        # print('time from', before, '~', startTime)

        result = df_sensor[(df_sensor['uid'] == current_uid)]

        result = result[result['Timestamp'] > before]
        result = result[result['Timestamp'] <= startTime]
        result = result.sort_values('Timestamp')
        # print(len(result))

        # calculate means of each sensor data
        sensor_avg = result[['dB', 'Temperature', 'Humidity', 'CO2', 'TVOC', 'Light', 'Human']].mean(axis=0).tolist()
        # print(sensor_avg)
        sensor_data.append(sensor_avg)

    df_final = pd.concat(
        [df, pd.DataFrame(sensor_data, columns=['dB', 'Temperature', 'Humidity', 'CO2', 'TVOC', 'Light', 'Human'])],
        axis=1)

    df_final = df_final.sort_values('startTime', ignore_index=True)
    return df_final
