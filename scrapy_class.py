
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time




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


	def _is_element_displayed(self, browser, elem_text, elem_type):
		if elem_type == "class":
			try:
				out = browser.find_element_by_class_name(elem_text).is_displayed()
			except:
				out = False
		elif elem_type == "css":
			try:
				out = browser.find_element_by_css_selector(elem_text).is_displayed()
			except (NoSuchElementException, TimeoutException):
				out = False
		else:
			raise ValueError("arg 'elem_type' must be either 'class' or 'css'")
		return(out)

	def check_for_captcha(self, browser):
		if self._is_element_displayed(browser, "captcha-container", "class"):
			print("\nCAPTCHA!\n"\
				  "Manually complete the captcha requirements.\n"\
				  "Once that's done, if the program was in the middle of scraping "\
				  "(and is still running), it should resume scraping after ~30 seconds.")
			self._pause_for_captcha(browser)


	def _pause_for_captcha(self, browser):
		while True:
			time.sleep(30)
			if not self._is_element_displayed(browser, "captcha-container", "class"):
				break


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
			#print("Other disign page")
			#####https://www.zillow.com/homes/for_sale//homedetails/295-N-Minnewawa-Ave-Fresno-CA-93727/18759515_zpid/
			#####https://www.zillow.com/homes/for_sale/2094098284_zpid/globalrelevanceex_sort/29.783524,-95.363388,29.650838,-95.474968_rect/12_zm/

			try:
				elm = browser.find_element_by_id('zestimate-details')
			except:
				print("Other disign page")
				self.check_for_captcha(browser)
				return zestimate , zRange, builtIn, builtBy, comName, parking

			elm.click()
			element_text = elm.text.split()
			#print(element_text.split())
			print(element_text)

			try:
				listIndex = element_text.index("Zestimate")
				print(listIndex)
				print(listIndex)
				#zestimate = element_text.split()[3]
				zestimate = element_text[listIndex+1]

				listIndex = element_text.index("RANGE")
				#zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])
				zRange = element_text[listIndex+1] + element_text[listIndex+2] + element_text[listIndex+3]
			except:
				zestimate = "NA"

			try:
				listIndex = element_text.index("Zestimate"[ listIndex[ len(element_text)]])
				print(listIndex)
			except:
				pass

			

			elm = browser.find_element_by_xpath("//*[@class='hdp-facts-expandable-container clear']") 
			element_text = elm.text.split('\n')
			#print(element_text)

			builtIn = element_text[4]
			builtBy = "NA"
			comName = element_text[2]
			parking = element_text[10]

			return zestimate , zRange, builtIn, builtBy, comName, parking



		elm.click()
		element_text = elm.text.split()
		#print(element_text.split())
		print(element_text)

		try:
			listIndex = element_text.index("Zestimate")
			print(listIndex)
			print(listIndex)
			#zestimate = element_text.split()[3]
			zestimate = element_text[listIndex+1]

			listIndex = element_text.index("RANGE")
			#zRange = str(element_text.split()[6] + element_text.split()[7] + element_text.split()[8])
			zRange = element_text[listIndex+1] + element_text[listIndex+2] + element_text[listIndex+3]
		except:
			zestimate = "NA"

		try:
			listIndex = element_text.index("Zestimate"[ listIndex[ len(element_text)]])
			print(listIndex)
		except:
			pass
				
	

			
		#print("zestimate: " + zestimate)
		#print("zRange: " + zRange)

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












