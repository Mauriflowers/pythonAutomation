from behave import given, then, when
from features.page_objects.base_page import click_element_by_css_selector, element_displayed, send_keys_by_css_selector, wait_until_element_displayed
from features.page_objects.login_page import LOGIN_BTN, PASS_FIELD, USERNAME_FIELD, LOGIN_FORM_BTN, LOGOUT_BTN
from features.utils.CommonConstants import VALID_PASSWORD, VALID_USERNAME, LOGIN_URL
from utils.Driver import launch_browser


@given('the user is on Demoblaze page')
def navigate_to_demoblaze(context):
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)


@when('the user logs in with valid credentials')
def login_with_valid_credentials(context):
    click_element_by_css_selector(context, LOGIN_BTN)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASS_FIELD, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_FORM_BTN)


@then('the page displays the log out button')
def logout_button_displayed(context):
    wait_until_element_displayed(context,LOGOUT_BTN )
    logout_button = element_displayed(context, LOGOUT_BTN)
    assert logout_button == True
