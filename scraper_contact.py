import time
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

def login_details(driver):
	
	driver.find_element_by_id('login_form_username').send_keys('public')
	driver.find_element_by_id('login_form_password').send_keys('public')


def add_contacts(my_message):
	driver = webdriver.Chrome()
	driver.get('https://www.xing.com/xtm/login')
	
	#login
	login_details(driver)
	#Need to select all the candidates you want to connect with
	result = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element_by_id("project-content"))
	time.sleep(5) # wait a little bit before the awesome code starts
	if result:
		for candidateCard in driver.find_elements_by_css_selector("div[data-testid='candidateCard']"):
			#click ...
			candidateCard.find_element_by_css_selector("button[data-testid='button-dropdown']").click()
			#add as contact if not already added
			if candidateCard.find_element_by_css_selector("button[data-testid='Add as contact'][class='kbkvTj']"):
				candidateCard.find_element_by_css_selector("button[data-testid='Add as contact']").click()
				#get the first name
				name = driver.find_element_by_css_selector(".emfPRz .jhyHrE .kQwify").text

				#insert the message
				first = name.split()[0]
				driver.find_element_by_css_selector("textarea[data-testid='textareaText']").send_keys(my_message.format(first))

				time.sleep(1)
				#send out invitation with message
				driver.find_element_by_class_name("iXuigZ").click()

				time.sleep(1)
		    

	driver.quit()


def send_inmails(my_subject, my_message):
	driver = webdriver.Chrome()
	driver.get('https://www.xing.com/xtm/login')

	pages = True
	
	#login
	login_details(driver)
	#Need to select all the candidates you want to connect with
	result = WebDriverWait(driver, timeout=180).until(lambda d: d.find_element_by_id("project-content"))
	time.sleep(5) # wait a little bit before the awesome code starts
	if result:

		while pages:
			for candidateCard in driver.find_elements_by_css_selector("div[data-testid='candidateCard']"):
				#click send message
				candidateCard.find_element_by_css_selector("button[class='WiHzd']").click()
				#send message if not done already
				if driver.find_element_by_css_selector("div[class='MainContainer-eVyIZs']"):
					#get the first name
					name = driver.find_element_by_css_selector("div[data-testid='to-recipient-unfocused']").text
					first = name.split()[0]

					driver.find_element_by_css_selector("input#subject").send_keys(my_subject.format(first))
					driver.find_element_by_css_selector("textarea[name='body']").send_keys(my_message.format(first))

					time.sleep(15)
					#send out invitation with message
					#driver.find_element_by_css_selector("button[data-testid='reply-button']").click()

					time.sleep(10)

					if driver.find_element_by_id('pagination') and driver.find_element_by_css_selector("li[data-testid='current-page-item'] + li"):
						driver.find_element_by_css_selector("li[data-testid='current-page-item'] + li").click()
					else: 
						pages = False

	driver.quit()