import csv
import pandas as pd

# data prepare
# file1: psytoday_diseases
def generate_today():
    file1 = open('specialties_detail3.txt', 'r')
    Lines = file1.readlines()
    
    count = 0
    with open('psytoday_diseases.csv', "w") as csv_file:
        writer = csv.writer(csv_file)
        for line in Lines:
            line = line.strip()
            writer.writerow([count,line])
            count += 1

# file2: wiki_diseases
def generate_wiki():
    df = pd.read_csv('wiki_diseases.csv', index_col = [0])
    df["item"] = df["item"].str.split("/").str[-1]
    df.to_csv('wiki.csv', index=False)

# file3 wiki_symptoms
def generate_symtom():
    df = pd.read_csv('allSymptoms_csv.csv', index_col = [0])
    df["symptoms"] = df["symptoms"].str.split("/").str[-1]
    df.to_csv('symptoms.csv', index=False)

# all id pairs
def generate_id_pairs():
    df_today = pd.read_csv('psytoday.csv', delimiter='\t')
    df_wiki = pd.read_csv('wiki.csv', delimiter='\t')
    row = []
    for today_id in df_today["id"]:
        for wiki_id in df_wiki["id"]:
            row.append([today_id, wiki_id])
    f = open('id_pairs.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['today.ID', 'wiki.ID'])
    for r in row:
        writer.writerow([r[0], r[1]])
    f.close()


# generate_today()
# generate_id_pairs()