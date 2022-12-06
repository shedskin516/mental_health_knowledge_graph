import pandas as pd
import re


def split_words(item):
    words = re.split(' |/|;', item)
    res = []
    for word in words:
        # word = word.lstrip('\"|\(')
        # word = word.rstrip('\"|\)')
        if word != '' and word != 'nan':
            res.append(word)
    return res

def cal():
    df_today = pd.read_csv('psytoday.csv')
    for item in df_today["name"]:
        item = str(item)
        list = split_words(item)
        print(list)
        for word in list:
            print(word)


# cal()