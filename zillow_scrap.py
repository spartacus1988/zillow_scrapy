import csv
import scrapy_class

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

	print(ZillowSpider.name)
	print(ZillowSpider.start_urls)

	#print(links)

