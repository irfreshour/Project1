import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class EmployeePage():
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def get_title(self):
        WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.ID, "employee_title")))
        return self.__driver.title

    def logout_button(self):
        time.sleep(5)
        return WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.ID, "lout1")))
