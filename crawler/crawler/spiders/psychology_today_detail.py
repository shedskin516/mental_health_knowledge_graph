import scrapy
from bs4 import BeautifulSoup

class MovieSpider(scrapy.Spider):
    name = "therapist_detail"

    # The range of crawling is line:[start, end) from filename
    filename = 'data/url_unique.txt'
    start = 0
    end = 9979
    file = open(filename, 'r')
    lines = file.readlines()
    start_urls = []
    for i in range(start, end):
        if i >= start and i < end:
            start_urls.append(lines[i].strip())
            print(lines[i].strip())
    # start_urls = ['https://www.psychologytoday.com/us/therapists/maureen-young-smith-corte-madera-ca/439519']

    def parse(self, response):
        title = ''.join(_.strip() for _ in response.xpath('//descendant::div[@class="profile-title"][2]/h2/span/descendant-or-self::*/text()').getall())
        title = ", ".join(title.split(","))
        mobile = response.xpath('//a[@id="phone-click-reveal"]/text()').get()
        if mobile is not None:
            mobile = mobile.strip()
        street = response.xpath('//div[@itemprop="address"]/span[@itemprop="streetAddress"]/text()').get()
        if street is not None:
            street = street.strip()
        yield {
            'url': response.url,
            'name': response.xpath('//h1[@itemprop="name"]/text()').get(),
            'title': title,
            'mobile': mobile,
            'street': street,
            'city': response.xpath('//div[@itemprop="address"]/span[@itemprop="addressLocality"]/text()').get()[:-1],
            'state': response.xpath('//div[@itemprop="address"]/span[@itemprop="addressRegion"]/text()').get(),
            'postalcode': response.xpath('//div[@itemprop="address"]/span[@itemprop="postalcode"]/text()').get(),
            'about': ' '.join(response.xpath('//div[@class="statementPara"]/text()').getall()),
            'website': response.xpath('//a[@data-event-label="website"]/@href').get(),
            'specialties': ', '.join([s.strip() for s in response.xpath('//ul[@class="attribute-list specialties-list"]/li/text()').getall()]),
            'issues': ', '.join([s.strip() for s in response.xpath('//div[@class="spec-list attributes-issues"]/div/ul/li/text()').getall()]),
            'mental_health': ', '.join([s.strip() for s in response.xpath('//div[@class="spec-list attributes-mental-health"]/div/ul/li/text()').getall()]),
            'ethnicity': ' '.join(_.strip() for _ in response.xpath('//div[@class="spec-subcat attributes-ethnicity-focus"]/descendant-or-self::*/text()').getall()),
            'age': ', '.join([s.strip() for s in response.xpath('//div[@class="spec-list attributes-age-focus"]/div/ul/li/text()').getall()]),
            'communities': ', '.join([s.strip() for s in response.xpath('//div[@class="spec-list attributes-categories"]/div/ul/li/text()').getall()]),
            'therapy_type': ', '.join(response.xpath('//div[@class="spec-list attributes-treatment-orientation"]/div/ul/li/span/text()').getall()),
            'modality': ', '.join([s.strip() for s in response.xpath('//div[@class="spec-list attributes-modality"]/div/ul/li/text()').getall()]),
        }


