from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CustomisedStatementPage(BasePage):
    _accno_input = (By.NAME, "accountno")
    _from_date_input = (By.NAME, "fdate")
    _to_date_input = (By.NAME, "tdate")
    _min_amount_input = (By.NAME, "amountlowerlimit")
    _num_trans_input = (By.NAME, "numtransaction")
    _submit_btn = (By.NAME, "AccSubmit")
    _reset_btn = (By.NAME, "res")
    _accno_msg = (By.ID, "message2")
    _from_date_msg = (By.ID, "message26")
    _to_date_msg = (By.ID, "message27")
    _min_amount_msg = (By.ID, "message12")
    _num_trans_msg = (By.ID, "message13")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php")

    def set_account_no(self, accno):
        self.send_keys(self._accno_input, str(accno))

    def set_from_date(self, date_str):
        self.send_keys(self._from_date_input, date_str)

    def set_to_date(self, date_str):
        self.send_keys(self._to_date_input, date_str)

    def set_min_amount(self, amount):
        self.send_keys(self._min_amount_input, str(amount))

    def set_num_transactions(self, num):
        self.send_keys(self._num_trans_input, str(num))

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_accno_validation_msg(self):
        return self.get_text(self._accno_msg) if self.driver.find_elements(*self._accno_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()
