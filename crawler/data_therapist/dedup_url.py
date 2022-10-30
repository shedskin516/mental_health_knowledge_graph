import pandas as pd
import re

myset = set()
filename = 'data/url_all.txt'
lines = open(filename, 'r').readlines()
for line in lines:
    url = line.strip()
    if url not in myset:
        myset.add(url)
        print(url)
