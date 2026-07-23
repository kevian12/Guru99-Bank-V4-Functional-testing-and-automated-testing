from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FundTransferPage(BasePage):
    _payers_input = (By.NAME, "payersaccount")
    _payees_input = (By.NAME, "payeeaccount")
    _amount_input = (By.NAME, "ammount")
    _desc_input = (By.NAME, "desc")
    _submit_btn = (By.NAME, "AccSubmit")
    _reset_btn = (By.NAME, "res")
    _payers_msg = (By.ID, "message10")
    _payees_msg = (By.ID, "message11")
    _amount_msg = (By.ID, "message1")
    _desc_msg = (By.ID, "message17")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/FundTransInput.php")

    def set_payers_account(self, accno):
        self.send_keys(self._payers_input, str(accno))

    def set_payees_account(self, accno):
        self.send_keys(self._payees_input, str(accno))

    def set_amount(self, amount):
        self.send_keys(self._amount_input, str(amount))

    def set_description(self, desc):
        self.send_keys(self._desc_input, desc)

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_payers_validation_msg(self):
        return self.get_text(self._payers_msg) if self.driver.find_elements(*self._payers_msg) else ""

    def get_amount_validation_msg(self):
        return self.get_text(self._amount_msg) if self.driver.find_elements(*self._amount_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()
