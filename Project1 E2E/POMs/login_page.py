from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage():
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def email_input(self):
        return self.__driver.find_element_by_id("email")

    def password_input(self):
        return self.__driver.find_element_by_id("pw")

    def login_button(self):
        return self.__driver.find_element_by_id("login_button")

    def check_title(self):
        return self.__driver.find_element_by_id("logHead")
