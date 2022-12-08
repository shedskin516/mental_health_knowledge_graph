import pandas as pd
import json

# df = pd.read_csv('drugs_list.csv')
# df['drugs'] = [item.split('/')[-1] for item in df['drugs']]
# df['drugsLabel'] = ['https://www.drugs.com/'+item+'.html' for item in df['drugsLabel']]

# print(df['drugs'])
# print(df['drugsLabel'])

# df.to_csv('url_list.csv', index=False)



# with open('drugs.json', 'r') as f:
#     data = json.load(f)
# df2 = pd.json_normalize(data)
# urls = df2["url"]
# myset = set()
# for url in urls:
#     if url not in myset:
#         myset.add(url.lower())
#     else:
#         print(url)
# print(len(myset))

# df = pd.read_csv('mapping_Q2url.csv')
# list = list(df["url"])
# print(len(list))
# for url in list:
#     if url.lower() not in myset:
#         print(url)



# with open('drugs.json', 'r') as f:
#     data = json.load(f)
# df = pd.json_normalize(data)
# df.to_csv('drugs.csv', sep="\t")



df = pd.read_csv('drugs.csv', sep="\t")

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

unique_item('brand_names')
unique_item('drug_classes')
unique_item('related_drugs')