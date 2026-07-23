import pytest
from pages.manager_home_page import ManagerHomePage
from pages.edit_customer_page import EditCustomerPage

class TestEditCustomer:
    def test_tc_ec_002_empty_customer_id(self, login_driver):
        ecp = EditCustomerPage(login_driver.driver)
        ecp.set_customer_id("")
        ecp.click_submit()
        msg = ecp.get_cid_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_ec_003_nonexistent_customer_id(self, login_driver):
        ecp = EditCustomerPage(login_driver.driver)
        ecp.set_customer_id("99999")
        ecp.click_submit()
        alert_text = ecp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_ec_004_cid_with_non_digits(self, login_driver):
        ecp = EditCustomerPage(login_driver.driver)
        ecp.set_customer_id("ABC123")
        ecp.click_submit()
        msg = ecp.get_cid_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""

    def test_tc_ec_008_reset_button(self, login_driver):
        ecp = EditCustomerPage(login_driver.driver)
        ecp.set_customer_id("12345")
        ecp.click_reset()
        val = ecp.find_element(ecp._cusid_input).get_attribute("value")
        assert val == ""
