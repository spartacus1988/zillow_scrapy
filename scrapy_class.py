import scrapy

class ZillowSpider(scrapy.Spider):
	def __init__(self, links):
		self.name = "zillow"
		self.allowed_domains = ["www.zillow.com"]
		self.start_urls = links
		print("ggg")

	def parse(self, response):
		print(response)
		for sel in response:#.xpath('//ul/li'):
			print("dddd")
			print(str(sel))
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			desc = sel.xpath('text()').extract()
			print(title)#, link, desc


	def start_requests(self):

		# urls = [
		#         'http://quotes.toscrape.com/page/1/',
		#         'http://quotes.toscrape.com/page/2/']
		# for url in urls:
		print("fffff")
		scrapy.Request(url="http://quotes.toscrape.com/page/1/", callback=self.parse)


