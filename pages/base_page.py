from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=10):
        self.find_clickable(locator, timeout).click()

    def send_keys(self, locator, text, timeout=10):
        el = self.find_element(locator, timeout)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def get_alert_text(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None

    def dismiss_alert(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert.dismiss()
        except TimeoutException:
            pass

    def accept_alert(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None
