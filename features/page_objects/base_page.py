from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_element_by_css_selector(self, css_selector):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).click()


def get_element_text(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).text


def send_keys_by_css_selector(self, css_selector, text):
    self.driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(text)


def wait_until_element_displayed(self, locator):
    WebDriverWait(self.driver, 2).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))


def wait_until_url_changes(self):
    WebDriverWait(self.driver, 2).until(expected_conditions.url_changes)


def element_not_displayed(self, css_selector):
    try:
        self.driver.find_element(By.CSS_SELECTOR, css_selector)
    except NoSuchElementException:
        return True


def element_displayed(self, css_selector):
    return self.driver.find_element(By.CSS_SELECTOR, css_selector).is_displayed()


def wait_until_alert_is_present(self):
    WebDriverWait(self.driver, 20).until(
        expected_conditions.alert_is_present())


def get_alert_text(self):
    return self.driver.switch_to.alert.text
