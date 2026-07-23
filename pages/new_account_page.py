from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NewAccountPage(BasePage):
    _cusid_input = (By.NAME, "cusid")
    _account_type = (By.NAME, "selaccount")
    _initial_deposit = (By.NAME, "inideposit")
    _submit_btn = (By.NAME, "button2")
    _reset_btn = (By.NAME, "reset")
    _cid_msg = (By.ID, "message14")
    _deposit_msg = (By.ID, "message19")
    _success_heading = (By.XPATH, "//p[@class='heading3']")
    _account_id_text = (By.XPATH, "//td[contains(text(),'Account ID')]/following-sibling::td")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")

    def set_customer_id(self, cid):
        self.send_keys(self._cusid_input, cid)

    def select_account_type(self, acct_type):
        from selenium.webdriver.support.ui import Select
        el = self.find_element(self._account_type)
        Select(el).select_by_visible_text(acct_type)

    def set_initial_deposit(self, amount):
        self.send_keys(self._initial_deposit, str(amount))

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def get_cid_validation_msg(self):
        return self.get_text(self._cid_msg) if self.driver.find_elements(*self._cid_msg) else ""

    def get_alert_message(self):
        return self.get_alert_text()

    def get_success_message(self):
        return self.get_text(self._success_heading) if self.driver.find_elements(*self._success_heading) else ""

    def get_account_id(self):
        return self.get_text(self._account_id_text) if self.driver.find_elements(*self._account_id_text) else ""
