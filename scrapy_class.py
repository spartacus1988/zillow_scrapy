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
		#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
		#options.add_argument("--start-maximized")
		#options.add_argument("allow-running-insecure-content")
		#options.add_argument("test-type")

		#options.add_argument("--headless")

		#options.add_argument("--disable-gpu") 

		browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)	

		browser.wait = WebDriverWait(browser, 10)

		return(browser)

	def _is_empty(self, obj):
		if any([len(obj) == 0, obj == "null"]):
			return(True)
		else:
			return(False)



	def get_zestimate(self, soup_obj):
		#with open("file.txt", "w") as file:
			#print(soup_obj, file=file)
		#print(soup_obj)
		zestimate = soup_obj.find("div", {"class" : "zestimate-value"})#.get_text().strip()
		print(zestimate)
		try:
			zestimate = soup_obj.find("div", {"class" : "main-row  home-summary-row"}).get_text().strip()
			print(zestimate)
			zestimate = soup_obj.find("div", class_="zestimate-value")#.get_text().strip()
			print(zestimate)
			zestimate = soup_obj.findAll("div", {"class": "zestimate-value"})
			print(zestimate)
		except (ValueError, AttributeError):
			zestimate = "NA"
		if self._is_empty(zestimate):
			zestimate = "NA"
		return(zestimate)



	def get_one_request(self, browser, url):

		browser.get(url)

		html = browser.page_source
		soup = BeautifulSoup(html, "lxml")
		#print(soup)
		#for tag in soup.find_all('title'):
			#print(tag.text)

		zestimate = self.get_zestimate(soup)
		print(zestimate)


		#browser.quit()