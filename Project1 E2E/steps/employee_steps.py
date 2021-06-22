from behave import given, when, then
import time


@then(u'user is on the employee page')
def step_impl(context):
    assert context.employee_page.get_title() == "Employee"


@when(u'user click on the logout button on the employee page')
def step_impl(context):
    time.sleep(1)
    context.employee_page.logout_button().click()
