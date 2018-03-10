#import json
#import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from selenium.common.exceptions import TimeoutException


class ZillowSpider:
	def __init__(self, links):
		self.links = links
		self.json = None
  


	def get_one_request(self, url):

		#browser = webdriver.Chrome('/usr/local/bin/chromedriver')
		options = Options()
		#options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
		#options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
		#options.add_argument("--start-maximized")
		#options.add_argument("allow-running-insecure-content")
		#options.add_argument("test-type")
		options.add_argument("--headless")
		#options.add_argument("--window-size=1920x1080")
		#options.add_argument("--disable-gpu") 

		browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)	
		browser.get('https://yandex.ru')

		html = browser.page_source
		soup = BeautifulSoup(html, "lxml")
		for tag in soup.find_all('title'):
			print(tag.text)


		browser.quit()