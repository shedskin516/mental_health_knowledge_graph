import pandas as pd
import re

df = pd.read_csv('therapist1.csv', sep="\t", index_col = [0])

newdf = []
for item in df['specialties_detail_1']:
    rowset = set()
    item = str(item).split("~")
    for words in item:
        words = re.split(',|/|;', words)
        for word in words:
            el = word.strip()
            if el != '' and el != 'nan':
                rowset.add(el)
    newitem = '~'.join(rowset)
    newdf.append(newitem)

newdf2 = []
for item in df['specialties_detail_2']:
    rowset = set()
    item = str(item).split("~")
    for words in item:
        if words != '' and words != 'nan':
            words = words.rstrip('\,')
            words = words.rstrip('\.')
            rowset.add(words)
    newitem = '~'.join(rowset)
    newdf2.append(newitem)

# black_list = ['older adults','young adults','children','elders']
black_list = []
newdf3 = []
for i in range(len(newdf)):
    newset = set()
    d1 = newdf[i].split("~")
    for item in d1:
        if item != '' and item != 'nan' and item.lower() not in black_list:
            newset.add(item)
    d2 = newdf2[i].split("~")
    for item in d2:
        if item != '' and item != 'nan' and item.lower() not in black_list:
            newset.add(item)
    newitem = '~'.join(newset)
    newdf3.append(newitem)
df['specialties_detail'] = newdf3

df = df.drop('specialties_detail_1', axis=1)
df = df.drop('specialties_detail_2', axis=1)

df = df.loc[:,['url','name','title','mobile','street','city','state','postalcode','about','website','specialities','specialties_detail','ethnicity','age','communities','therapy_type','modality']]


myset = set()
for item in df['specialties_detail']:
    words = item.split('~')
    for word in words:
        if word != '' and words != 'nan':
            myset.add(word)

df.to_csv('therapist_merged.csv', sep="\t")

with open('specialties_detail.txt', 'w') as the_file:
    for w in myset:
        the_file.write(w+'\n')
