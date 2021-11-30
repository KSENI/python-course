import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	go_element = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	go_element.click()
	alert = browser.switch_to.alert
	alert.accept()

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	anser_element = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", anser_element)
	anser_element.send_keys(y)
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()

	alert_end = browser.switch_to.alert
	print(alert_end.text)
finally:
	browser.quit()