from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from BioScraper.items import Website


'''
def TextCleaner(raw):
    length = len(raw) 
    cleaned = ""
    inText = False
    front = True
    lastChar = ""
    currentChar = ""
    for i in length:

        currentChar = raw[i]

        if currentChar == '<':
            lastChar = currentChar
            inText = False
        elif currentChar == '>':
            lastChar = currentChar
            inText = True
        elif ((currentChar != '>') and (currentChar != '/')) and (lastChar == '<'):
            front = True

        elif ((currentChar == '>') or (currentChar == '/')) and (lastChar == '<'):
            front = False

        elif ((currentChar != '<') and (currentChar != '>')) and inText == True:
'''





class DmozSpider(Spider):
    name = "neb"
    allowed_domains = ["neb.com"]
    start_urls = ["https://www.neb.com/tools-and-resources/search?type=Protocol&num=1000"]

    ''' {{{{not used}}}}
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//nav[@class="pagination"]')
        next_urls = []

        base_url = "https://www.neb.com"
        tempName = sites.xpath('//li/*[text()[contains(.,"next")]][1]/@href').extract()
        tempName = tempName[0]
        tempName = base_url + tempName

        for temp in tempName:
            next_urls.append(temp)

        requestList = []
        for url in next_urls:
            request = Request(url, callback=self.parse)
            requestList.append(request)

        return requestList
        '''

    def parse(self, response):


        sel = Selector(response)
        sites = sel.xpath('//section[@class="search-results"]')
        secondary_urls = []

        for site in sites:
            tempName = site.xpath('//td/a/@href').extract()
        
        for temp in tempName:
            secondary_urls.append(temp)

        requestList = []
        for url in secondary_urls:
            request = Request(url, callback=self.nebPage)
            requestList.append(request)
        
        return requestList

    def nebPage(self, response):

        sel = Selector(response)
        sites = sel.xpath('//section[@class="primary"]')
        items = []

        for site in sites:

            item = Website()

            item['title'] = site.xpath('//header[@class="group"]/h1/text()').extract()


            body_els = ""
            item['body']= site.xpath('.//div[@class="inner"]/descendant::*').extract()

            items.append(item)

        return items
        
        



 