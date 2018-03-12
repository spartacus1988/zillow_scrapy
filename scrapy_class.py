
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait




class ZillowSpider:
	def __init__(self, links):
		self.links = links
  


	def init_driver(file_path):
		options = Options()
		#options.add_argument("--headless")
		browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)	

		browser.wait = WebDriverWait(browser, 10)

		return(browser)

	def _is_empty(self, obj):
		if any([len(obj) == 0, obj == "null"]):
			return(True)
		else:
			return(False)



	def get_one_request(self, browser, url):
		zestimate = "NA"
		zRange = "NA"
		builtIn = "NA"
		builtBy = "NA"
		comName = "NA"
		parking = "NA"

		browser.get(url)
		browser.implicitly_wait(1)

		try:
			elm = browser.find_element_by_id('homeValue')
			#elm = browser.find_element_by_id('home-details-module-zone')
			

		except:
			print("Other disign page")
			#####https://www.zillow.com/homes/for_sale//homedetails/295-N-Minnewawa-Ave-Fresno-CA-93727/18759515_zpid/
			#####https://www.zillow.com/homes/for_sale/2094098284_zpid/globalrelevanceex_sort/29.783524,-95.363388,29.650838,-95.474968_rect/12_zm/

			elm = browser.find_element_by_id('zestimate-details')
			elm.click()
			element_text = elm.text
			#print(element_text.split())
			#print(element_text)
			zestimate = element_text.split()[3]
			zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])
			#print("zestimate: " + zestimate)
			#print("zRange: " + zRange)

			elm = browser.find_element_by_xpath("//*[@class='hdp-facts-expandable-container clear']") 
			element_text = elm.text.split('\n')
			#print(element_text)

			builtIn = element_text[4]
			builtBy = "NA"
			comName = element_text[2]
			parking = element_text[10]

			return zestimate , zRange, builtIn, builtBy, comName, parking



		elm.click()
		element_text = elm.text
		#print(element_text.split())
		zestimate = element_text.split()[3]
		zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])

		elm = browser.find_element_by_xpath("//*[@class='hdp-facts zsg-content-component']") 
		element_text = elm.text.split('\n')

		for strIng in element_text:
			if "Built in" in strIng:
				strIng = strIng.replace("Built in",'')
				#print("Built in: " + str)
				builtIn = strIng
			if "Built by" in strIng:
				strIng = strIng.replace("Built by:",'')
				#print("Built by: " + str)
				builtBy = strIng
			if "Community name" in strIng:
				strIng = strIng.replace("Community name:",'')
				#print("Community name: " + str)
				comName = strIng
			if "Parking" in strIng:
				strIng = strIng.replace("Parking:",'')
				#print("Parking: " + str)
				parking = strIng

		return zestimate , zRange, builtIn, builtBy, comName, parking












