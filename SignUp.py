import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome("driver/chromedriver.exe")  # type: WebDriver
driver.get("https://www.surveymonkey.com/")
time.sleep(10)

driver.find_element(By.XPATH,("//a[contains(text(),'SIGN UP')]")).click()

username = driver.find_element_by_id('username')
username.send_keys("1okpriyaj")

password = driver.find_element_by_id('password')
password.send_keys("16priyajain")

email = driver.find_element_by_id('email')
password.send_keys("priya@gmail.com")

firstname = driver.find_element_by_id('first_name')
password.send_keys("priya")

lastname = driver.find_element_by_id('last_name')
password.send_keys("jain")

driver.find_element(By.XPATH, '//button[@type=\'submit\']').click()

driver.quit()