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


	ZillowSpider = scrapy_class.ZillowSpider(links)
	browser = ZillowSpider.init_driver()
	#browser.implicitly_wait(15)

	
	#zestimate , zRange = ZillowSpider.get_zestimate(browser, links[0])
	#print("zestimate: " + zestimate)
	#print("zRange: " + zRange)




	browser.get(links[0])

	#elm = browser.find_elements_by_xpath('//div[contains(text(), "' + Facts + '")]')
	#elm = browser.find_element_by_css_selector('fact-group-container zsg-content-component top-facts')
	#elm = browser.find_element_by_tag_name('h3')
	#elm = browser.find_element_by_class_name('fact-group-container zsg-content-component top-facts')
	#elm = browser.find_element_by_css_selector(".fact-group-container zsg-content-component top-facts")
	#elm = browser.find_element_by_id('yui_3_18_1_1_1520845064328_9721')

	#elm = browser.find_element_by_xpath("//*[@class='fact-group-container zsg-content-component top-facts']") 


	#elm = browser.find_element_by_xpath("//*[@class='zsg-content_collapsed zsg-h4']") 


	#elm = browser.find_element_by_xpath("//*[@class='zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1']") 

	#elm = browser.find_element_by_css_selector('ul.zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1')


	#elm = browser.find_element_by_xpath("//*[@class='fact-group-container zsg-content-component top-facts']//*[@class='zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1']") 

	#elm = browser.find_element_by_css_selector('div.fact-group-container zsg-content-component top-facts')

	#elm = browser.find_element_by_xpath("//*[@class='fact-group-container zsg-content-component top-facts']") 

	elm = browser.find_element_by_xpath("//*[@class='hdp-facts zsg-content-component']") 




	

	
	#browser.implicitly_wait(2)
	#elm.click()

	element_text = elm.text
	print(element_text)
	# print(type(element_text))
	# print(element_text.split())
	# print(element_text.split()[3])
	# print(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])
	#zestimate = element_text.split()[3]
	#zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])






