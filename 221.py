import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
	a = num1_element.text
	num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
	b = num2_element.text
	c = int(a) + int(b)
	print(c)
	select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
	select.select_by_value(str(c))
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()
finally:
	time.sleep(10)
	browser.quit()

