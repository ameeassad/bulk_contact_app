import time
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException


def add_contacts(my_message):
	driver = webdriver.Chrome()
	driver.get('https://www.xing.com/xtm/login')

	pages = True
	
	#Need to select all the candidates you want to connect with
	result = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element_by_id("project-content"))
	time.sleep(3) # wait a little bit before the awesome code starts
	if result:
		while pages:
			for candidateCard in driver.find_elements_by_css_selector("div[data-testid='candidateCard']"):
				time.sleep(5)
				#click ...
				candidateCard.find_element_by_css_selector("button[data-testid='button-dropdown']").click()
				#add as contact if not already added
				if candidateCard.find_element_by_css_selector("button[data-testid='Add as contact']"):
					candidateCard.find_element_by_css_selector("button[data-testid='Add as contact']").click()
					
					try: 
						#candidateCard.find_element_by_css_selector("div[data-testid='lightbox-overlay']")
						#get the first name
						name = driver.find_element_by_css_selector("div[data-testid='lightbox-overlay'] section > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text

						#insert the message
						first = name.split()[0]
						driver.find_element_by_css_selector("textarea[data-testid='textareaText']").send_keys(my_message.format(first))

						time.sleep(5)
						#send out invitation with message
						element = driver.find_element_by_css_selector("div[data-testid='lightbox-overlay'] div > div > div > button")
						driver.execute_script("arguments[0].click();", element)

					except NoSuchElementException: 
						continue

			try:	
				if driver.find_element_by_id('pagination'):
					driver.find_element_by_css_selector("li[data-testid='current-page-item'] + li").click()
				else: 
					pages = False
			except NoSuchElementException:
				pages = False
				break

	driver.quit()


def send_inmails(my_subject, my_message):
	driver = webdriver.Chrome()
	driver.get('https://www.xing.com/xtm/login')

	pages = True
	
	#login

	#Need to select all the candidates you want to connect with
	result = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element_by_id("project-content"))
	time.sleep(3) # wait a little bit before the awesome code starts
	if result:

		while pages:
			for candidateCard in driver.find_elements_by_css_selector("div[data-testid='candidateCard']"):
				time.sleep(5)
				#click send message
				candidateCard.find_element_by_css_selector("div[data-testid='card-header'] div[data-testid='internal-header'] > div:nth-child(2) > div > button ").click()
				#send message if not done already
				try:
					form = driver.find_element_by_css_selector("form")
					#get the first name
					name = form.find_element_by_css_selector("div[data-testid='to-recipient-unfocused']").text
					first = name.split()[0]

					form.find_element_by_css_selector("input#subject").send_keys(my_subject.format(first))
					form.find_element_by_css_selector("textarea[name='body']").send_keys(my_message.format(first))

					time.sleep(5)

					#send out invitation with message
					element = driver.find_element_by_css_selector("button[data-testid='reply-button']")
					driver.execute_script("arguments[0].click();", element)

				except NoSuchElementException:
					continue

			try:	
				if driver.find_element_by_id('pagination'):
					driver.find_element_by_css_selector("li[data-testid='current-page-item'] + li").click()
				else: 
					pages = False
			except NoSuchElementException:
				pages = False
				break

	driver.quit()