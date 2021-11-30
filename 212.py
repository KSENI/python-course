from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	x_element = browser.find_element(By.CSS_SELECTOR, "img[src='images/chest.png']")
	x = x_element.get_attribute("valuex")
	y = calc(x)
	anser_element = browser.find_element(By.ID, "answer")
	anser_element.send_keys(y)
	im_the_robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
	im_the_robot_checkbox.click()
	robots_rule_element = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
	robots_rule_element.click()
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()
	
finally:
    time.sleep(10)
    browser.quit()