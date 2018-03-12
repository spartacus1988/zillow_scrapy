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
	elm = browser.find_element_by_xpath("//*[@class='hdp-facts zsg-content-component']") 
	element_text = elm.text.split('\n')

	print(element_text)

	# for str in element_text:
	# 	if "Built in" in str:
	# 		print("Built in: " + str.split()[2])
	# 	if "Built by" in str:
	# 		print("Built by: " + str.split()[2] + " " + str.split()[3])
	# 	if "Community name " in str:
	# 		print("Community name: " + str.split()[2])
	# 	if "Parking" in str:
	# 		print("Parking: " + str.split()[2] + " " + str.split()[3])



	for str in element_text:
		if "Built in" in str:
			str = str.replace("Built in",'')
			print("Built in: " + str)
		if "Built by" in str:
			str = str.replace("Built by:",'')
			print("Built by: " + str)
		if "Community name" in str:
			str = str.replace("Community name:",'')
			print("Community name: " + str)
		if "Parking" in str:
			str = str.replace("Parking:",'')
			print("Parking: " + str)









	# print(type(element_text))
	# print(element_text.split())
	# print(element_text.split()[3])
	# print(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])
	#zestimate = element_text.split()[3]
	#zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])






