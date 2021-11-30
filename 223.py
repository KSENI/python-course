import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	first_name_element = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
	first_name_element.send_keys("Ivan")
	last_name_element = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
	last_name_element.send_keys("Ivanov")
	email_element = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
	email_element.send_keys("Ivanov@dfsdf.com")
	short_bio_element = browser.find_element(By.CSS_SELECTOR, "#file")
	current_dir = os.path.abspath("/Users/a18881415/Desktop/selenium_course/223.txt")
	print(current_dir)
	file_path = os.path.join(current_dir)
	print(file_path)
	short_bio_element.send_keys(file_path)
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()
finally:
	time.sleep(10)
	browser.quit()