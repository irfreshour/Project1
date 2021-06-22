from behave import given, when, then


@given(u'user is on the login page')
def step_impl(context):
    assert context.driver.title == "Login"


@when(u'user clicks on email input')
def step_impl(context):
    context.login_page.email_input().click()


@when(u'user types {word} in the email input')
def step_impl(context, word: str):
    context.login_page.email_input().send_keys(word)


@when(u'user clicks on password input')
def step_impl(context):
    context.login_page.password_input().click()


@when(u'user types {word} into password input')
def step_impl(context, word: str):
    context.login_page.password_input().send_keys(word)


@when(u'user presses submit button')
def step_impl(context):
    context.login_page.login_button().click()



