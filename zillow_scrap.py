import csv
import scrapy_class
from bs4 import BeautifulSoup
#from lxml import etree


def csv_reader(file_obj):
	links = []
	reader = csv.reader(file_obj)

	for row in reader:
		#print(" ".join(row))
		#print(row[10])
		#links.insert(0, row[10])
		links.append(row[10])
		#links.pop(0)
	links = links[1:]
	return links








if __name__ == "__main__":

	csv_path = "2018-03-09_162252.csv"
	with open(csv_path, "r") as f_obj:
		links = csv_reader(f_obj)


	# with open('file.html', 'r') as file:
	# 	#ssoup = BeautifulSoup(file.read(), 'html.parser')
	# 	ssoup = BeautifulSoup(file.read(), "lxml")
		#print(ssoup)
	#zestimate = ssoup.find("span", {"itemprop" : "streetAddress"}).get_text().strip()
	#zestimate = ssoup.find("div", {"class": "yui3-widget yui3-lightbox yui3-widget-positioned yui3-widget-stacked yui3-lightbox-modal yui3-lightbox-focused"})#.get_text().strip()

	#zestimate = ssoup.find("div", {"class": "yui3-widget yui3-lightbox yui3-widget-positioned yui3-widget-stacked yui3-lightbox-modal yui3-lightbox-focused"})
	
	#zestimate = zestimate.find("div", {"class": "dialog yui3-lightbox-content"})

	#zestimate = zestimate.find("div", {"class": "yui3-widget-bd lightbox-body zsg-tooltip-viewport"})


	#zestimate = ssoup.find("div", {"class": "zsg-tooltip-viewport"})
	
	#zestimate = ssoup.find("div", {"id": "home-details-module-zone"})

	#zestimate = ssoup.find(id="homeValue")

	# <section class="home-details-collapsible-component-CollapsibleContainer collapsed collapsible" id="homeValue">
	# 	<h2 class="zsg-h2 hdp-collapsible-title">Home Value</h2>
	# 	<div class="collapsible-content"></div>
	# </section>




	#zestimate = ssoup.find("div", {"class" : "zestimate-value"})#.get_text().strip()
	#print(zestimate.prettify())




	ZillowSpider = scrapy_class.ZillowSpider(links)

	browser = ZillowSpider.init_driver()

	#browser.implicitly_wait(15)

	browser.get(links[0])

	elm = browser.find_element_by_id('homeValue')
	browser.implicitly_wait(2)
	elm.click()

	element_text = elm.text
	print(element_text)
	print(type(element_text))
	print(element_text.split())
	print(element_text.split()[3])
	print(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])



	#ZillowSpider.get_one_request(browser, links[0] )
	






