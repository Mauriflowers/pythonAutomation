from multiprocessing import context
from behave import given, then, when
from features.page_objects.base_page import click_element_by_css_selector, element_displayed, get_element_text, send_keys_by_css_selector, wait_until_url_changes
from features.page_objects.login_page import LOGIN_BTN, LOGIN_URL
from features.utils.CommonConstants import FIELD_PASS, FIELD_USERNAME, LOGIN_BUTTON, LOGOUT_BUTTON, USER_LOG, VALID_PASSWORD, VALID_USERNAME
from utils.Driver import launch_browser
import time

@given('the user is on Demoblaze page')
def navigate_to_demoblaze(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)
    time.sleep(2)
    

@when('the user logs in with valid credentials')
def login_with_valid_credentials(context) :
    click_element_by_css_selector(context, LOGIN_BTN)
    send_keys_by_css_selector(context, FIELD_USERNAME, VALID_USERNAME)
    send_keys_by_css_selector(context, FIELD_PASS, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BUTTON)
    time.sleep(2)

@then ('the page shows the log out button')
def logout_button_displayed(context) :
    logout_button = element_displayed(context, LOGOUT_BUTTON)
    assert logout_button == True
   
@then ('the page shows the welcome button')
def user_welcome_button_displayed(context) :
    user_welcome = element_displayed (context,USER_LOG)
    assert user_welcome == True