from behave import then, when
from features.page_objects.base_page import click_element_by_css_selector, element_displayed, wait_until_url_changes
from features.page_objects.cart_page import DELETEPRODUCT1_BTN
from features.page_objects.header_page import ADDTOOCART1_BTN, CART_BTN, PRODUCT1_BTN


@when('the user add a product to the cart')
def add_product_to_cart(context):
    click_element_by_css_selector(context, PRODUCT1_BTN)
    wait_until_url_changes(context)
    click_element_by_css_selector(context, ADDTOOCART1_BTN)

@then ('the cart shows the product inside') 
def cart_show_product_inside (context):
    click_element_by_css_selector(context, CART_BTN)
    wait_until_url_changes(context)
    delete_product_btn = element_displayed(context,DELETEPRODUCT1_BTN)
    assert delete_product_btn == True
