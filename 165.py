from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    firstName.send_keys("Ivan")
    secondName = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    secondName.send_keys("Ivanov")
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("ivanov@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
