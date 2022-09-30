from multiprocessing import context
from behave import given, then, when
from features.page_objects.base_page import click_element_by_css_selector, element_displayed, get_alert_text, get_element_text, send_keys_by_css_selector, wait_until_alert_is_present, wait_until_url_changes
from features.page_objects.contact_page import CONTACT_EMAIL, CONTACT_NAME, MAIL_FIELD, MESSAGE, MESSAGE_FIELD, NAME_FIELD, SEND_MESSAGE_BTN
from features.page_objects.login_page import LOGIN_BTN, LOGIN_URL
from features.utils.CommonConstants import CONTACT_BTN, FIELD_PASS, FIELD_USERNAME, LOGIN_BUTTON, LOGOUT_BUTTON, USER_LOG, VALID_PASSWORD, VALID_USERNAME
from utils.Driver import launch_browser
import time

@given ('the user is on contact button')
def navigate_to_demoblaze(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)
    click_element_by_css_selector(context, CONTACT_BTN)
    time.sleep(2)

@when ('the user sends a message')
def complete_the_contact_form(context) :
    send_keys_by_css_selector(context, CONTACT_EMAIL, MAIL_FIELD)
    send_keys_by_css_selector(context, CONTACT_NAME, NAME_FIELD)
    send_keys_by_css_selector(context, MESSAGE, MESSAGE_FIELD)
    click_element_by_css_selector(context, SEND_MESSAGE_BTN)
    time.sleep(2)

@then ('the page confirm message is displayed')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Thanks for the message!!'
