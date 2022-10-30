import pandas as pd
import re

df = pd.read_csv('therapist.csv', sep="\t")

def unique_item(name):
    myset = set()
    for item in df[name]:
        list = str(item).split(",")
        for el in list:
            el = el.strip()
            # el = re.sub("^[^\w\s]|[^\w\s]$", "", el)
            if el != '' and el != 'nan':
                myset.add(el)
    with open(name+'.txt', 'w') as the_file:
        for w in myset:
            the_file.write(w+'\n')

unique_item('specialties')
unique_item('issues')
unique_item('mental_health')
unique_item('age')
unique_item('communities')
unique_item('therapy_type')
unique_item('modality')
