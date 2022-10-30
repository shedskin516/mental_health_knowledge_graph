import pandas as pd
import json

with open('therapist.json', 'r') as f:
    data = json.load(f)
df = pd.json_normalize(data)

df['about'] = df['about'].str.replace('\n',' ')
df['about'] = df['about'].str.replace('\r','')
df['about'] = df['about'].str.replace('\u2028',' ')

df.to_csv('therapist.csv', sep="\t")