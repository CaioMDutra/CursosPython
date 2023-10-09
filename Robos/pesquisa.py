from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

pesquisa = input("O que deseja pesquisar? ")

driver = webdriver.Chrome()
site = driver.get("https://www.google.com.br ")
site = driver.find_element(by=By.XPATH, value=('//*[@id="APjFqb"]')).send_keys(pesquisa)
site = driver.find_element(by=By.XPATH, value=('//*[@id="APjFqb"]')).send_keys(Keys.RETURN)
#time.sleep(5000)

results =  driver.find_element(by=By.XPATH, value=('//*[@id="result-stats"]'))
print(results.text)