import rltk
import csv
from csv import reader
import sys
from minineedle import needle, smith, core

# You can use this tokenizer in case you need to manipulate some data
tokenizer = rltk.tokenizer.crf_tokenizer.crf_tokenizer.CrfTokenizer()

class TodayRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['id']

    @rltk.cached_property
    def title(self):
        return self.raw_object['name'].lower()

    @rltk.cached_property
    def title_tokens(self):
        return set(tokenizer.tokenize(self.title))

class WikiRecord(rltk.Record):
    def __init__(self, raw_object):
        super().__init__(raw_object)
        self.name = ''

    @rltk.cached_property
    def id(self):
        return self.raw_object['id']

    @rltk.cached_property
    def title(self):
        return self.raw_object['name'].lower()

    @rltk.cached_property
    def title_tokens(self):
        return set(tokenizer.tokenize(self.title))

def is_pair(r1, r2, threshold):
    c = rltk.jaro_winkler_similarity(r1.title, r2.title)
    # c = rltk.hybrid_jaccard_similarity(r1.title_tokens, r2.title_tokens)
    # c = rltk.tf_idf_similarity()

    # # smith waterman
    # alignment = smith.SmithWaterman(r1.title, r2.title)
    # alignment.align()
    # c = alignment.get_score()   

    # print(c)
    return c > threshold, c

def compare_dev(ds_today, ds_wiki, threshold):
    dev_set_file = 'gt.csv'
    dev = []
    with open(dev_set_file, encoding='utf-8', errors="replace") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if len(row) > 1 and idx > 0:
                dev.append(row)
    gt = rltk.GroundTruth()
    for row in dev:
        # print(row[0],row[1])
        r1 = ds_today.get_record(row[0])
        r2  = ds_wiki.get_record(row[1])
        if row[-1] == '1':
            gt.add_positive(r1.raw_object['id'], r2.raw_object['id'])
        else:
            gt.add_negative(r1.raw_object['id'], r2.raw_object['id'])
    trial = rltk.Trial(gt)

    for r_today, r_wiki in rltk.get_record_pairs(ds_today, ds_wiki, ground_truth=gt):
        result, _ = is_pair(r_today, r_wiki, threshold)
        if result:
            trial.add_positive(r_today, r_wiki)
        else:
            trial.add_negative(r_today, r_wiki)
    trial.evaluate()

    print('precison:', trial.precision, 'recall:', trial.recall, 'f-measure:', trial.f_measure)
    print('tp:', len(trial.true_positives_list))
    print('fp:', len(trial.false_positives_list))
    print('tn:', len(trial.true_negatives_list))
    print('fn:', len(trial.false_negatives_list))

def entity_linking(ds_today, ds_wiki, threshold):
    output_name = 'jaro_symptom.csv'
    f = open(output_name, 'w')
    writer = csv.writer(f)
    writer.writerow(['today.ID', 'wiki.ID', 'today.name', 'wiki.name', 'confidence', 'result'])
    f.close()
    prev = ''
    count = 1
    for r_today, r_wiki in rltk.get_record_pairs(ds_today, ds_wiki):
        if r_today != prev:
            prev = r_today
            print(count)
            count += 1
        result, confidence = is_pair(r_today, r_wiki, threshold)
        f = open(output_name, 'a')
        writer = csv.writer(f)
        writer.writerow([r_today.id, r_wiki.id, r_today.title, r_wiki.title, confidence, result])
        f.close()

def main():
    if len(sys.argv) > 1:
        threshold = float(sys.argv[1])
    else:
        threshold = 0.91

    today_file = 'psytoday.csv'
    wiki_file = 'symptoms.csv'
    ds_today = rltk.Dataset(rltk.CSVReader(today_file),record_class=TodayRecord)
    ds_wiki = rltk.Dataset(rltk.CSVReader(wiki_file),record_class=WikiRecord)

    # compare_dev(ds_today, ds_wiki, threshold)

    entity_linking(ds_today, ds_wiki, threshold)



if __name__ == "__main__":
    main()
