import tensorflow as tf
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import LeaveOneOut
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from ast import literal_eval

import shap
import re


def sensor_data_preprocessing(df):
    # 센서 데이터 결측값 확인
    # print('Missing Values')
    # print('=' * 60)
    # print(df.isna().sum())

    # 센서 데이터 결측값 대체
    df.sort_values('uid', inplace=True)
    cols = ['dB', 'Temperature', 'Humidity', 'CO2', 'TVOC', 'Light', 'Human']
    df.loc[:, cols] = df.loc[:, cols].bfill()
    df = df.dropna()
    # print(df.info())

    # 센서 데이터 정규화
    sensor_data = df[cols]
    normalized = (sensor_data - sensor_data.mean()) / sensor_data.std()
    normalized = normalized.round(3)

    result = df.copy()
    result[cols] = normalized

    # print(result.info())
    return result


def columns_cleaning(df):
    df.sort_index(inplace=True)

    # delete unnecessary cols
    # cols_deleted = ['answers', 'sceneStartTimes', 'sceneEndTimes', 'endTime',
    #                 'interaction_methods(binary)', 'whole_interaction_length(sec)', 'PHQ-9', 'GAD-7', 'Gender']
    # df = DATASET.drop(cols_deleted, axis=1)
    # print(df.columns.tolist())

    before_audio = df['before_audio']
    response_audio = df['response_audio']

    # print(df.isnull().sum())
    # 각 행을 1차원 array로 변환
    pre_audio = before_audio.apply(lambda x: np.array(literal_eval(x)).flatten())
    voice_audio = response_audio.apply(lambda x: np.array(literal_eval(x)).flatten())
    # print(type(pre_audio))

    # columns 정의
    df = df[['uid', 'whole_conv_length(sec)', 'dixit_response_rate',
             'dB', 'Temperature', 'Humidity', 'CO2', 'TVOC', 'Light', 'Human',
             # 'before_audio', 'response_audio',
             'F', 'M', 'Extroversion', 'Agreeableness', 'Conscientiousness', 'Neuroticism', 'Openness',
             'depression_or_not', 'anxietyDisorder_or_not',
              'PSS_score', 'PSS_stress_or_not',
             'phq2_result', 'gad2_result',
             'stress_result', 'posNeg_result'
             ]]

    df['uid'] = df['uid'].astype(int)
    return df, pre_audio, voice_audio


def preprocessing(df, pre_audio, voice_audio, voice_use):
    target_labels = ['phq2_result', 'gad2_result', 'stress_result', 'posNeg_result']

    # uid list
    uid_lst = df['uid'].tolist()
    # print('uid_lst', uid_lst)

    # define X and y dataset
    X = df.drop(target_labels, axis=1)
    X = X.drop(['uid'], axis=1)
    print('X columns (Extracted Features):', X.columns)
    y = df[target_labels]

    # transform data frame X and y into numpy array
    # print('X shape :', X.shape)
    X = np.asarray(X).astype('float32')

    # print('X array:', X)

    # X 데이터 정규화
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    # print('X shape :', X_scaled.shape)
    # print('X array:', X_scaled)

    y = np.asarray(y).astype('float32')
    # print('y array:', y)
    # print('y shape :', y.shape)

    df_pre_audio = pd.DataFrame(pre_audio.values.tolist(), index=pre_audio.index)
    df_pre_audio = np.asarray(df_pre_audio).astype('float32')

    df_voice_audio = pd.DataFrame(voice_audio.values.tolist(), index=voice_audio.index)
    df_voice_audio = np.asarray(df_voice_audio).astype('float32')

    # multi label arrays
    # y_stress = y[:, 0]
    # y_posNeg = y[:, 1]

    # print(X)
    # print(df_voice_audio)
    # print(df_pre_audio)

    # VOICE 사용하려면 아래 주석 해제
    # NaN 제거
    if voice_use is True:
        X = np.hstack((X, df_pre_audio, df_voice_audio))
        X = X[~np.isnan(X).any(axis=1)]
        y_temp = np.hstack((y, df_pre_audio, df_voice_audio))
        y_temp = y_temp[~np.isnan(y_temp).any(axis=1)]
        y = y_temp[:, :2]

    print(X.shape)
    print(y.shape)
    return X, y


def smote(X, y):  # 데이터 불균형 해소 - 오버샘플링
    smote = SMOTE(random_state=42)
    X_train = X
    y_train = y
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    print('SMOTE 적용 전 학습용 피처/레이블 데이터 세트: ', X_train.shape, y_train.shape)
    # print('SMOTE 적용 전 레이블 값 분포: \n', pd.Series(y_train).value_counts())
    print('SMOTE 적용 후 학습용 피처/레이블 데이터 세트: ', X_train_resampled.shape, y_train_resampled.shape)
    print('SMOTE 적용 후 레이블 값 분포: \n', pd.Series(y_train_resampled).value_counts())
    return X_train_resampled, y_train_resampled


def predict(X, y):

    cv = LeaveOneOut()

    # create model
#     models = [svm.SVC(kernel='rbf'), LogisticRegression(), KNeighborsClassifier(n_neighbors=2),
#               DecisionTreeClassifier(), GaussianNB(), RandomForestClassifier(random_state=42)]
   models = [svm.SVC(kernel='rbf'), KNeighborsClassifier(),
              DecisionTreeClassifier(), GaussianNB(), RandomForestClassifier(random_state=42)]
    
    for i in models:
        model = i
        print('Model: %s' % model)
        # evaluate model
        scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv)
        # report performance
        print('Accuracy: %.3f (%.3f)' % (scores.mean(), scores.std()))




if __name__ == '__main__':
    # PATH = 'data.pkl'
    # DATASET = pickle.load(open(PATH, mode='rb'))
    #
    # # one-hot encoding: gender
    # gender = pd.get_dummies(DATASET['Gender'])
    # DATASET = pd.concat([DATASET, gender], axis=1)
    # # print(DATASET.info())
    #
    # # preprocess missing values
    # DATASET = sensor_data_preprocessing(DATASET)
    #
    # # drop missing values
    # DATASET.dropna(inplace=True)
    #
    # # columns 정리
    # DATASET, pre_audio, voice_audio = columns_cleaning(DATASET)
    # # print(DATASET.info())
    #
    # X, y = preprocessing(DATASET, pre_audio, voice_audio)
    #
    # # pickle_path = 'features.pkl'
    # # with open(pickle_path, "wb") as file:
    # #     pickle.dump(X, file)

    tf.random.set_seed(42)
    PATH = 'features_X.pkl'
    X = pickle.load(open(PATH, mode='rb'))


    PATH = 'features_y.pkl'
    y = pickle.load(open(PATH, mode='rb'))

    # voice feature 사용 여부
    voice_use = False

  
    # predict mental status
    phq_X_train_resampled, phq_y_train_resampled = smote(X, y[:, 0])
    gad_X_train_resampled, gad_y_train_resampled = smote(X, y[:, 1])
    stress_X_train_resampled, stress_y_train_resampled = smote(X, y[:, 2])
    panas_X_train_resampled, panas_y_train_resampled = smote(X, y[:, 3])

    print("=" * 60)
    print("PHQ")
    # predict(phq_X_train_resampled, phq_y_train_resampled)

    print("=" * 60)
    print("GAD")
    predict(gad_X_train_resampled, gad_y_train_resampled)

    print("=" * 60)
    print("Stress")
    predict(stress_X_train_resampled, stress_y_train_resampled)

    print("=" * 60)
    print("POS & NEG")
    predict(panas_X_train_resampled, panas_y_train_resampled)

