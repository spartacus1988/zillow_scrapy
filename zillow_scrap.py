import csv
import scrapy_class
from bs4 import BeautifulSoup
import pandas as pd
import time



def update_csv_cell(ZillowSpider, browser):

	filepath = "2018-03-09_162252.csv"

	with open(filepath, 'r+') as csvfile:
		reader = csv.reader(csvfile)
		lines = []
		i=0

		for current_line in reader:
			#print(current_line)
			# i+=1
			# if i == 4:
			# 	break

			if current_line[10] == 'url':
				print(current_line)
				current_line.append('zestimate')
				current_line.append('zRange')
				current_line.append('builtIn')
				current_line.append('builtBy')
				current_line.append('comName')
				current_line.append('parking')
				lines.append(current_line)
			else:
				zestimate , zRange, builtIn, builtBy, comName, parking = ZillowSpider.get_one_request(browser, current_line[10])
				print(current_line[10])
				current_line.append(zestimate)
				current_line.append(zRange)
				current_line.append(builtIn)
				current_line.append(builtBy)
				current_line.append(comName)
				current_line.append(parking)
				lines.append(current_line)


	# Write data to data frame, then to CSV file.
	file_name = "%s_%s.csv" % (str(time.strftime("%Y-%m-%d")),
                           str(time.strftime("%H%M%S")))
	columns = ["address", "city", "state", "zip", "price", "sqft", "bedrooms",
           "bathrooms", "days_on_zillow", "sale_type", "url", "zestimate", "zRange", "builtIn", "builtBy", "comName", "parking"]
	pd.DataFrame(lines, columns = columns).to_csv(file_name, index = False)





if __name__ == "__main__":



	ZillowSpider = scrapy_class.ZillowSpider()
	browser = ZillowSpider.init_driver()

	update_csv_cell(ZillowSpider, browser)








