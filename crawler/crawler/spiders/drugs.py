import scrapy
from bs4 import BeautifulSoup
import pandas as pd
import re

class Drugs(scrapy.Spider):
    name = "drugs"
    df = pd.read_csv('data_drugs/url_list.csv')
    start_urls = list(df.iloc[:,1])

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find("h1").text.strip()

        subtitle = soup.find("p", class_="drug-subtitle")
        
        gname_label = subtitle.find("b", text="Generic name:")
        gname = ''
        if gname_label:
            gname = gname_label.next_sibling
            gname = gname.split('[')[0].strip()

        bname_label = subtitle.find("b", text=re.compile('Brand name'))
        bname = ''
        if bname_label:
            for elt in bname_label.nextSiblingGenerator():
                if elt.name == 'br':
                    break
                else:
                    bname = bname + elt.text

        drug_class_label = subtitle.find("b", text=re.compile('Drug class'))
        drug_class = ''
        if drug_class_label:
            for elt in drug_class_label.nextSiblingGenerator():
                if elt.name == 'p':
                    break
                else:
                    drug_class = drug_class + elt.text

        use = soup.find("h2", id="uses")
        use_content = ''
        if use:
            for elt in use.nextSiblingGenerator():
                if elt.name == 'h2':
                    break
                if elt.name == 'p':
                    use_content = use_content + ' ' + elt.text

        warning = soup.find("h2", id="warnings")
        warning_content = ''
        if warning:
            for elt in warning.nextSiblingGenerator():
                if elt.name == 'h2':
                    break
                if elt.name == 'p':
                    warning_content = warning_content + ' ' + elt.text

        related_drug = soup.find("h2", text=re.compile('Related/similar drugs'))
        related_drug_content = ''
        if related_drug:
            for elt in related_drug.nextSiblingGenerator():
                if elt.name == 'h2':
                    break
                else:
                    related_drug_content = related_drug_content + elt.text

        yield {
            'url': response.url,
            'name': name,
            'generic_name': gname,
            'brand_names': bname.strip(),
            'drug_classes': drug_class.strip(),
            'description': use_content.strip(),
            'warnings': warning_content.strip(),
            'related_drugs': related_drug_content.strip(),
        }

