from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome("C:\\Users\\isaac\\chromedriver.exe")

driver.get("file:///C:/Users/isaac/PycharmProjects/frontend/login.html")
