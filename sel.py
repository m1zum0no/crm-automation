from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait

# Login credentials
login = input("login: ")
password = input("password: ")
link = input("link: ")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(link)
driver.maximize_window()
time.sleep(1)


# Logging in 
driver.find_element('name', 'login').send_keys(login)
driver.find_element('name', 'password').send_keys(password)
driver.find_element('xpath', "//*[@type='submit']").click()
