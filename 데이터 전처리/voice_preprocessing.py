import csv
import os
import pandas as pd
from datetime import datetime


def voice_integration(df):
    csv_path = os.path.join("voice_data.csv")
    df_voice = pd.read_csv(csv_path)
    df_voice.sort_values('Timestamp', ignore_index=True)
    # print(df_voice.info())
    df_voice.sort_values('Timestamp')

    result = pd.DataFrame()

    for i in range(0, len(df)):

        current_uid = int(df['uid'][i])
        startTime = int(df['startTime'][i])  # sec
        endTime = int(df['endTime'][i])

        start = startTime - 60 * 1 * 1000  # 사전; 시작 1분 전
        end = startTime

        # print("uid", current_uid)
        # print("time from", datetime.fromtimestamp(start/1000), ' ', datetime.fromtimestamp(end/1000), start, '~', end)
        pre_result = df_voice[(df_voice['uid'] == current_uid)]
        pre_result = pre_result[(pre_result['Timestamp'] >= start) & (pre_result['Timestamp'] <= end)]
        pre_result.sort_values('Timestamp')

        # endTime 으로부터 2분 전 ~ endTime
        end = endTime
        start = end - 60 * 2 * 1000

        post_result = df_voice[(df_voice['uid'] == current_uid)]
        post_result = post_result[(post_result['Timestamp'] >= start) & (post_result['Timestamp'] <= end)]
        post_result_index = post_result.index[(post_result['Timestamp'] >= start) & (post_result['Timestamp'] <= end)].tolist()
        print(post_result.index)

        if len(post_result_index) == 0:
            print(current_uid, endTime, datetime.fromtimestamp(end/1000))

        if len(post_result_index) == 1:
            target_index = post_result_index[0]
            post_result = df_voice.iloc[target_index-1:target_index+1]
        post_result = post_result.sort_values('Timestamp')

        if len(list(pre_result['features'])) != 0 and len(list(post_result['features'])) != 0:
            # print(list(pre_result['features'])[0])

            voice = {
                # 'Timestamp': startTime,
                # 'uid': current_uid,
                'before_audio': list(pre_result['features'])[0],     # 설문 전 소리 녹음 데이터
                'response_audio': list(post_result['features'])[0]   # 설문 시 소리 녹음 데이터
            }

            df_audio = pd.DataFrame.from_dict([voice])
            result = pd.concat([result, df_audio], ignore_index=True)

    output = pd.concat([df, result], axis=1)
    output = output.sort_values('startTime', ignore_index=True)

    print(output.isna())
    return output
