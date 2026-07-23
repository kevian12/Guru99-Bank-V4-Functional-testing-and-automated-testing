from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BalanceEnquiryPage(BasePage):
    _accno_input = (By.NAME, "accountno")
    _submit_btn = (By.NAME, "AccSubmit")
    _reset_btn = (By.NAME, "res")
    _accno_msg = (By.ID, "message2")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/BalEnqInput.php")

    def set_account_no(self, accno):
        self.send_keys(self._accno_input, str(accno))

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_accno_validation_msg(self):
        return self.get_text(self._accno_msg) if self.driver.find_elements(*self._accno_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()
