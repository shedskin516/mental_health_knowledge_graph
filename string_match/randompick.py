import pandas as pd
import random

def keep_percent(threshold):
    rand = random.random()
    return rand < threshold

def get_gt():
    df = pd.read_csv('needleman.csv')
    sample = df.sample(n=2000000)
    keep_list = []
    count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
    for index, row in sample.iterrows():
        confidence = row['confidence']
        if confidence < 0.2:  # 0~0.2 20
            keep = keep_percent(0.00001)
            count1 += 1
        elif confidence < 0.4: # 0.2~0.4 70
            keep = keep_percent(0.005)
            count2 += 1
        elif confidence < 0.6: # 0.4~0.6 100
            keep = keep_percent(0.1)
            count3 += 1
        elif confidence < 0.8: # 0.6~0.8 64
            keep = keep_percent(1)
            count4 += 1
        else: # 0.8~1 24
            keep = keep_percent(1)
            count5 += 1
        if keep:
            keep_list.append(index)
    print(count1, count2, count3, count4, count5)

    df_new = df.iloc[keep_list,:]
    df_new = df_new.sort_values('confidence')
    df_new.to_csv('gt.csv', index=False)

get_gt()
