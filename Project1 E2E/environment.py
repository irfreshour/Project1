from behave.runner import Context
from selenium import webdriver
from POMs.login_page import LoginPage
from POMs.employee_page import EmployeePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("C:\\Users\\isaac\\chromedriver.exe")
    context.driver.get("file:///C:/Users/isaac/PycharmProjects/frontend/login.html")
    context.login_page = LoginPage(context.driver)
    context.employee_page = EmployeePage(context.driver)


def after_all(context: Context):
    context.driver.quit()
