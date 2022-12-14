import pandas as pd
import ast
import numpy as np
import locale
import os
from datetime import datetime
from datetime import timedelta
import time
import pickle


def log_filter(log_type):
    response_data_path = "./response_data.json"
    df = pd.read_json(response_data_path)

    logType = []
    startTime = []
    uid = []

    # END Log
    answers = []
    sceneStartTimes = []
    sceneEndTimes = []
    interactionMethods = []

    for i in range(len(df)):
        jsonPayload = df['jsonPayload'][i]

        if jsonPayload['logType'] == log_type:
            if 'uid' in jsonPayload.keys():  # uid 없는 로그가 있음
                logType.append(jsonPayload['logType'])
                startTime.append(jsonPayload['startTime'])
                uid.append(jsonPayload['uid'])

                if log_type == 'END':
                    answers.append(jsonPayload['answers'])
                    sceneStartTimes.append(jsonPayload['sceneStartTime'])
                    sceneEndTimes.append(jsonPayload['endTime'])
                    interactionMethods.append(jsonPayload['interactionMethod'])

    if log_type == 'START':
        filtered_log = pd.DataFrame({'uid': uid, 'logType': logType, 'startTime': startTime})
    else:
        filtered_log = pd.DataFrame({'uid': uid, 'logType': logType, 'startTime': startTime, 'answers': answers,
                                     'sceneStartTimes': sceneStartTimes, 'sceneEndTimes': sceneEndTimes,
                                     'interactionMethods': interactionMethods})
        # filtered_log = pd.DataFrame(
        #     {'uid': uid, 'logType': logType, 'startTime': startTime, 'answers': answers,
        #      'sceneStartTimes': sceneStartTimes, 'sceneEndTimes': sceneEndTimes})

    filtered_log = filtered_log.sort_values('startTime', ignore_index=True)

    return filtered_log


def log_integration(df_start, df_end):
    # combine START and END log
    uid = []
    startTime = []

    answers = []
    sceneStartTimes = []
    sceneEndTimes = []
    endTime = []

    interactionMethods = []
    num_people = 10

    for i in range(len(df_start)):

        # START 로그의 timestamp & UID 가 동일한 END 로그 찾기
        idx = df_end.index[
            (df_end['startTime'] == df_start['startTime'][i]) & (df_end['uid'] == df_start['uid'][i])].tolist()

        if len(idx) != 0:
            index = idx[0]
            # values from df_start
            uid.append(df_start['uid'][i])
            startTime.append(df_start['startTime'][i])

            # values from df_end
            answers.append(df_end['answers'][index])  # string list
            sceneStartTimes.append(df_end['sceneStartTimes'][index])  # string to num list
            sceneEndTimes.append(df_end['sceneEndTimes'][index])  # string to num list

            endTime.append(sceneEndTimes[-1][-1])  # sceneEndTimes 마지막 요소
            interactionMethods.append(df_end['interactionMethods'][index])

    df_start_end = pd.DataFrame({'uid': uid, 'startTime': startTime, 'answers': answers, 'sceneStartTimes':
        sceneStartTimes, 'sceneEndTimes': sceneEndTimes, 'endTime': endTime, 'interactionMethods': interactionMethods})

    df_start_end = df_start_end.sort_values('startTime', ignore_index=True)
    # print(len(df_start_end))

    uid_lst = list(range(1, num_people + 1))
    uid_lst = list(map(str, uid_lst))
    # print(uid_lst)

    # df_complete; 끝까지 완성된 대화
    df_complete = df_start_end[~df_start_end.isnull().any(axis=1)]  # select rows that does not contain any nan values
    df_complete = df_complete.sort_values('startTime', ignore_index=True)
    # print(df_complete)

    # UID 조건
    df_complete = df_complete[df_complete['uid'].isin(uid_lst)]  # select rows that has uid from 1~10
    df_complete = df_complete.sort_values('startTime', ignore_index=True)
    # print(df_complete)

    return df_complete


def get_response_time(df):  # (endTimes, startTimes) => df_times(각 씬별 소요시간 나타대는  df )

    # extract endTimes, startTimes and interaction StartTime
    endTimes = list(df['sceneEndTimes'])  # 2d-arr
    startTimes = list(df['sceneStartTimes'])  # 2d-arr
    startTime = np.array(df['startTime'])  # 1d-arr : 대화 시작 시간

    response_time_per_questions = []  # response time per questions
    whole_conv_lengths_lst = []

    for i in range(len(df)):
        whole_conv_length = (endTimes[i][-1] - startTime[i]) / 1000.0  # 전체 대화 시간(초)
        whole_conv_lengths_lst.append(whole_conv_length)

        # 각 대화별 질문 응답 시간
        res_intervals_per_conv = (np.array(endTimes[i]) - np.array(
            startTimes[i])) / 1000.0  # 초 단위 e.g. [13.4, 29.4, 10.02, 4, 5]
        response_time_per_questions.append(res_intervals_per_conv)

    response_time_arr = np.array(response_time_per_questions)  # 통계값 계산을 위해 list에서 arr 로 변형
    whole_conv_lengths_arr = np.array(whole_conv_lengths_lst)

    # 통계값 계산 : 각 대화별 소요시간 & 각 질문별 소요시간 --> input이 uid 별로 df일 때 활용
    sum_per_conv = response_time_arr.sum(axis=1)  # axis = 1: sum by rows(conv) #각 대화별 소요 시간

    return response_time_arr, sum_per_conv, whole_conv_lengths_lst


def get_response_rate(df_complete):
    dixit_response_rate = []
    interaction_methods = []  # 1 button ,0 voice
    phq2_result = []
    gad2_result = []
    stress_result = []
    mood_result = []

    for i in range(0, len(df_complete)):
        # for i in range(0,3):
        answers = df_complete['answers'][i]
        likert_answers = answers[:-1]
        likert_answers = list(map(int, likert_answers))  # string to int
        dixit_answer = answers[-1]
        dixit_response_time = df_complete['dixit(sec)'][i]  # sec

        # phq2
        if likert_answers[0] + likert_answers[1] >= 3:  # 합이 3 이상일 경우 주요 우울 장애가 있을 확률이 있다.
            phq2_result.append(1)   #1 : significant level of depression
        else:
            phq2_result.append(0)   #0 : no significant level of depression

        # gad2
        if likert_answers[2] + likert_answers[3] >= 2:  # 합이 3 이상일 경우 불안 장애
            gad2_result.append(1)   #1 : significant level
        else:
            gad2_result.append(0)   #0 : no significant level

        # STRESS LEVEL 1,0
        if likert_answers[4] >= 0:  # 0점 보다 크면, stress 있다고 판단
            stress_result.append(1) #1 : significant level of stress
        else:
            stress_result.append(0) #0 : no significant of stress
        # mood LEVEL
        if likert_answers[5] <= 0:  # 숫자가 음수이면, 부정 감정
            mood_result.append(1) #1 : bad mood
        else:
            mood_result.append(0) #0 : good mood


        # dixitResponseRate
        # if dixit_answer.contains('+'): #추가
        #  reprompt_or_not.append(1)
        dixit_answer = dixit_answer.replace('+', '')
        dixit_response_length = len(dixit_answer)
        dixit_response_rate_ = round(dixit_response_time / dixit_response_length, 3)
        dixit_response_rate.append(dixit_response_rate_)

        # interactionMethods
        interaction_methods_txt = df_complete['interactionMethods'][i]
        interaction_methods_binary_per_row = []
        for j in range(len(interaction_methods_txt)):
            if interaction_methods_txt[j] == 'buttons':
                interaction_methods_binary_per_row.append(1)
            elif interaction_methods_txt[j] == 'voice':
                interaction_methods_binary_per_row.append(0)
        interaction_methods.append(interaction_methods_binary_per_row)

    return interaction_methods, dixit_response_rate, phq2_result, gad2_result, stress_result, mood_result


def response_data():
    start = log_filter('START')
    # print(start.columns)
    end = log_filter('END')
    # print(end.columns)
    df_complete = log_integration(start, end)

    response_time_arr, whole_interaction_lengths, whole_conv_lengths_lst = get_response_time(df_complete)
    df_complete['phq1(sec)'], df_complete['phq2(sec)'], df_complete['gad1(sec)'], df_complete['gad2(sec)'], df_complete[
        'stress(sec)'], df_complete['posneg(sec)'], df_complete['dixit(sec)'] = response_time_arr.T
    df_complete['whole_interaction_length(sec)'] = whole_interaction_lengths
    df_complete['whole_conv_length(sec)'] = whole_conv_lengths_lst

    interaction_methods, dixit_response_rate, phq2_result, gad2_result, stress_result, mood_result = get_response_rate(df_complete)
    df_complete['interaction_methods(binary)'] = interaction_methods
    df_complete['dixit_response_rate'] = dixit_response_rate
    df_complete['phq2_result'] = phq2_result
    df_complete['gad2_result'] = gad2_result
    df_complete['stress_result'] = stress_result
    df_complete['posNeg_result'] = mood_result

    return df_complete
