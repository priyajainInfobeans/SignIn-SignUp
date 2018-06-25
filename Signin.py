import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome("driver/chromedriver.exe")
driver.get("https://www.surveymonkey.com/")
time.sleep(10)

driver.find_element(By.XPATH, "//a[contains(text(),'LOG IN')]").click()

username = driver.find_element_by_id('username')
username.send_keys("1000priyaj")

password = driver.find_element_by_id('password')
password.send_keys("16priyajain")

driver.find_element(By.XPATH, '//button[@type=\'submit\']').click()
driver.quit()