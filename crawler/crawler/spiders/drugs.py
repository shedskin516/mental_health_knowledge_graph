import scrapy
from bs4 import BeautifulSoup

class Drugs(scrapy.Spider):
    name = "drugs"
    
    start_urls = [
        'https://www.drugs.com/trazodone.html',
        # 'https://www.drugs.com/aripiprazole.html',
        # 'https://www.drugs.com/clonazepam.html'
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        use = soup.find("h2", id="uses")
        use_content = ''
        for elt in use.nextSiblingGenerator():
            if elt.name == 'h2':
                break
            if elt.name == 'p':
                use_content = use_content + elt.text

        yield {
            'use': use_content
        }

