from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DeleteCustomerPage(BasePage):
    _cusid_input = (By.NAME, "cusid")
    _submit_btn = (By.NAME, "AccSubmit")
    _reset_btn = (By.NAME, "res")
    _cid_msg = (By.ID, "message14")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/DeleteCustomerInput.php")

    def set_customer_id(self, cid):
        self.send_keys(self._cusid_input, cid)

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_cid_validation_msg(self):
        return self.get_text(self._cid_msg) if self.driver.find_elements(*self._cid_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()

    def accept_delete(self):
        return self.accept_alert()

    def dismiss_delete(self):
        self.dismiss_alert()
