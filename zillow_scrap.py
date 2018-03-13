import csv
import scrapy_class
from bs4 import BeautifulSoup



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



	#####https://www.zillow.com/homes/for_sale//homedetails/295-N-Minnewawa-Ave-Fresno-CA-93727/18759515_zpid/

	for url in links:	
		#zestimate , zRange, builtIn, builtBy, comName, parking = ZillowSpider.get_one_request(browser, "https://www.zillow.com/homes/for_sale//homedetails/295-N-Minnewawa-Ave-Fresno-CA-93727/18759515_zpid/")
		zestimate , zRange, builtIn, builtBy, comName, parking = ZillowSpider.get_one_request(browser, url)
		print("zestimate: " + zestimate)
		print("zRange: " + zRange)
		print("builtIn: " + builtIn)
		print("builtBy: " + builtBy)
		print("comName: " + comName)
		print("parking: " + parking)
		#break

		







