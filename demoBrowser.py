import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#Chrome driver service Selenium 160-> 160 chrome driver

service_obj= Service(r"C:\Users\moham\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")


time.sleep(2)




# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)