from behave import then, when
from features.page_objects.base_page import click_element_by_css_selector, get_alert_text, send_keys_by_css_selector, wait_until_alert_is_present
from features.page_objects.contact_page import CONTACT_EMAIL_FIELD, CONTACT_NAME_FIELD, CONTACT_BTN, MESSAGE_FIELD, SEND_MESSAGE_BTN
from features.utils.CommonConstants import MESSAGE_TEXT, CONTACT_NAME, CONTACT_EMAIL


@when('the user sends a message')
def complete_the_contact_form(context):
    click_element_by_css_selector(context, CONTACT_BTN)
    send_keys_by_css_selector(context, CONTACT_EMAIL_FIELD, CONTACT_EMAIL)
    send_keys_by_css_selector(context, CONTACT_NAME_FIELD, CONTACT_NAME)
    send_keys_by_css_selector(context, MESSAGE_FIELD, MESSAGE_TEXT)
    click_element_by_css_selector(context, SEND_MESSAGE_BTN)


@then('the page displays a confirmation message')
def alert_is_displayed(context):
    wait_until_alert_is_present(context)
    alert_text = get_alert_text(context)
    assert alert_text == 'Thanks for the message!!'
