import scrapy
from bs4 import BeautifulSoup

class MovieSpider(scrapy.Spider):
    name = "therapist_list"
    
    base_url = 'https://www.psychologytoday.com/us/therapists/california'
    start_urls = []
    total_page_num = 500
    for i in range(1, total_page_num+1):
        start_urls.append(base_url+'?page='+str(i))

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lists = soup.find_all("div", class_="results-row")
        for item in lists:
            a = item.find("div", class_="results-row-info").find("a")
            print(a["href"])

