from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ChangePasswordPage(BasePage):
    _old_pwd_input = (By.NAME, "oldpassword")
    _new_pwd_input = (By.NAME, "newpassword")
    _confirm_pwd_input = (By.NAME, "confirmpassword")
    _submit_btn = (By.NAME, "sub")
    _reset_btn = (By.NAME, "res")
    _old_pwd_msg = (By.ID, "message20")
    _new_pwd_msg = (By.ID, "message21")
    _confirm_pwd_msg = (By.ID, "message22")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/PasswordInput.php")

    def set_old_password(self, pwd):
        self.send_keys(self._old_pwd_input, pwd)

    def set_new_password(self, pwd):
        self.send_keys(self._new_pwd_input, pwd)

    def set_confirm_password(self, pwd):
        self.send_keys(self._confirm_pwd_input, pwd)

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_old_pwd_validation_msg(self):
        return self.get_text(self._old_pwd_msg) if self.driver.find_elements(*self._old_pwd_msg) else ""

    def get_new_pwd_validation_msg(self):
        return self.get_text(self._new_pwd_msg) if self.driver.find_elements(*self._new_pwd_msg) else ""

    def get_confirm_pwd_validation_msg(self):
        return self.get_text(self._confirm_pwd_msg) if self.driver.find_elements(*self._confirm_pwd_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()
