from behave import given, then, when
from features.page_objects.base_page import click_element_by_css_selector, element_displayed, get_alert_text, get_element_text, send_keys_by_css_selector, wait_until_alert_is_present, wait_until_url_changes
from features.page_objects.contact_page import CONTACT_EMAIL, CONTACT_EMAIL_FIELD, CONTACT_NAME, CONTACT_NAME_FIELD, MESSAGE, MESSAGE_TEXT, SEND_MESSAGE_BTN
from features.page_objects.login_page import LOGIN_URL
from features.utils.CommonConstants import CONTACT_BTN
from utils.Driver import launch_browser
import time

@when ('the user sends a message')
def complete_the_contact_form(context) :
    click_element_by_css_selector(context, CONTACT_BTN)
    send_keys_by_css_selector(context, CONTACT_EMAIL_FIELD, CONTACT_EMAIL)
    send_keys_by_css_selector(context, CONTACT_NAME_FIELD, CONTACT_NAME)
    send_keys_by_css_selector(context, MESSAGE_TEXT, MESSAGE)
    click_element_by_css_selector(context, SEND_MESSAGE_BTN)

@then ('the page displays a confirmation message')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Thanks for the message!!'
