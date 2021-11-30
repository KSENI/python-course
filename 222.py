import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	anser_element = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", anser_element)
	anser_element.send_keys(y)
	im_the_robot_checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
	im_the_robot_checkbox.click()
	robots_rule_element = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
	robots_rule_element.click()
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()
finally:
	time.sleep(10)
	browser.quit()