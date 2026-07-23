from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    _uid_input = (By.NAME, "uid")
    _pwd_input = (By.NAME, "password")
    _login_btn = (By.NAME, "btnLogin")
    _reset_btn = (By.NAME, "btnReset")
    _uid_msg = (By.ID, "message23")
    _pwd_msg = (By.ID, "message18")

    def __init__(self, driver):
        super().__init__(driver)
        from test_data.config import BASE_URL
        self.driver.get(BASE_URL)

    def set_uid(self, uid):
        self.send_keys(self._uid_input, uid)

    def set_password(self, pwd):
        self.send_keys(self._pwd_input, pwd)

    def click_login(self):
        self.click(self._login_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_uid_validation_msg(self):
        return self.get_text(self._uid_msg) if self.driver.find_elements(*self._uid_msg) else ""

    def get_pwd_validation_msg(self):
        return self.get_text(self._pwd_msg) if self.driver.find_elements(*self._pwd_msg) else ""

    def login(self, uid, pwd):
        self.set_uid(uid)
        self.set_password(pwd)
        self.click_login()

    def get_alert_message(self):
        return self.get_alert_text()
