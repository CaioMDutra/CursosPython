from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://registro.br")
driver.find_element(by=By.XPATH, value=('//*[@id="is-avail-field"]')).send_keys("roboscompython.com.br")
driver.find_element(by=By.XPATH, value=('//*[@id="is-avail-field"]')).send_keys(Keys.RETURN)
time.sleep(8)
