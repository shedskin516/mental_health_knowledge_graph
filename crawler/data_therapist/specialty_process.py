import pandas as pd
import re

df = pd.read_csv('therapist3.csv', sep="\t", index_col = [0])

newdf = []
for item in df['specialties_detail']:
    rowset = set()
    item = str(item).split("~")
    for words in item:
        rx_comma = re.compile(r",(?![^(]*\))")
        words = rx_comma.split(words)
        for word in words:
            el = word.strip()
            if el != '' and el != 'nan':
                rowset.add(el.lower())
    newitem = '~'.join(rowset)
    newdf.append(newitem)

df['specialties_detail'] = newdf

myset = set()
for item in newdf:
    words = item.split('~')
    for word in words:
        if word != '' and words != 'nan':
            myset.add(word.lower())

df.to_csv('therapist4.csv', sep="\t")

with open('specialties_detail3.txt', 'w') as the_file:
    for w in myset:
        the_file.write(w+'\n')
