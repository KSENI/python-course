import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def getResultCode():
	alert_end = browser.switch_to.alert
	alert_end_array = alert_end.text.split()
	result = alert_end_array[len(alert_end_array)-1]
	print(result)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
def resolveEquation():
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	anser_element = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", anser_element)
	anser_element.send_keys(y)
def clickSubmit():
	submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
	submit.click()

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.implicitly_wait(12)
	browser.get(link)
	button = browser.find_element(By.ID, "book")
	goodPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
	button.click()
	resolveEquation()
	clickSubmit()
	getResultCode()
finally:
	browser.quit()