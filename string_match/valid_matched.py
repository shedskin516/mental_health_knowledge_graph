import pandas as pd

input_file = 'jaro_symptom.csv'
df = pd.read_csv(input_file)

rslt_df = df[df['confidence'] > 0.91]

rslt_df.to_csv('valid_pairs_symptom.csv', index=False)

