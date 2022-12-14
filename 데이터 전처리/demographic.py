import os
import pandas as pd

def demographics(df_final):
    #demographics 전처리
    demographics_path = os.path.join('user_demographics.csv')
    demo = pd.read_csv(demographics_path)

    demographics_mtx = []
    for i in range(len(df_final)):
        uid = int(df_final['uid'][i])

        # select user demographic from demo dataframe with specific uid!
        d = demo[demo['uid'] == uid]  # d is df
        demographics_per_row = d.values[0][1:]  # d is converted to array!

        demographics_mtx.append(demographics_per_row)

    df_final = pd.concat([df_final, pd.DataFrame(demographics_mtx,
                                                 columns=['Gender', 'Extroversion', 'Agreeableness',
                                                          'Conscientiousness',
                                                          'Neuroticism', 'Openness', 'PHQ-9', 'depression_or_not',
                                                          'GAD-7',
                                                          'anxietyDisorder_or_not', 'PSS_pos_score', 'PSS_neg_score',
                                                          'PSS_score',
                                                          'PSS_stress_or_not'])], axis=1)


    return df_final