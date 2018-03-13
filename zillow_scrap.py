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



	listt = ['Home', 'Value', 'The', 'list', 'price', 'and', 'Zestimate', 'for', 'this', 'home', 'are', 'very', 'different,', 'so', 'we', 'might', 'be', 'missing', 'something.', 'Zestimate', '$295,177', 'ZESTIMATE', 'RANGE', '$263,000', '-', '$357,000', 'LAST', '30', 'DAY', 'CHANGE', '-$925', '(-0.3%)', 'Zestimate', 'history', '&', 'details']
	print(listt)
	try:
		listIndex = listt.index("Zestimate")
		print(listIndex)
		zestimate = listt[listIndex+1]
		if zestimate == "for":
			print("for")
			listt = listt[listIndex+1:]
			print(listt)

			listIndex = listt.index("Zestimate")
			print(listIndex)
			zestimate = listt[listIndex+1]
			print(zestimate)


		listIndex = listt.index("RANGE")
		zRange = listt[listIndex+1] + listt[listIndex+2] + listt[listIndex+3]
	except:
		zestimate = "NA"

	try:
		listIndex = listt.index("Zestimate"[ listIndex[ len(listt)]])
		print(listIndex)
	except:
		pass







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

		







