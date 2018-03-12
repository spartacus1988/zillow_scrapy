#import json
#import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

#from selenium.common.exceptions import TimeoutException


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
		zestimate = None
		zRange = None
		builtIn = None
		builtBy = None
		comName = None
		parking = None

		browser.get(url)

		elm = browser.find_element_by_id('homeValue')
		elm.click()
		element_text = elm.text
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





	def get_one_requests(self, browser, url):

		browser.get(url)

		html = browser.page_source
		soup = BeautifulSoup(html, "lxml")
		#print(soup)
		#for tag in soup.find_all('title'):
			#print(tag.text)

		zestimate = self.get_zestimate(soup)
		print(zestimate)


		#browser.quit()