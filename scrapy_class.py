import scrapy

class ZillowSpider(scrapy.Spider):
     def __init__(self, links):
        self.name = "zillow"
        self.allowed_domains = ["www.zillow.com"]
        self.start_urls = links

        def parse(self, response):
            for sel in response.xpath('//ul/li'):
                title = sel.xpath('a/text()').extract()
                link = sel.xpath('a/@href').extract()
                desc = sel.xpath('text()').extract()
                print(title)#, link, desc