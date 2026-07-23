import pytest
from pages.delete_customer_page import DeleteCustomerPage

class TestDeleteCustomer:
    def test_tc_dc_002_empty_customer_id(self, login_driver):
        dcp = DeleteCustomerPage(login_driver.driver)
        dcp.set_customer_id("")
        dcp.click_submit()
        msg = dcp.get_cid_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_dc_003_nonexistent_customer_id(self, login_driver):
        dcp = DeleteCustomerPage(login_driver.driver)
        dcp.set_customer_id("99999")
        dcp.click_submit()
        alert_text = dcp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_dc_004_cid_with_non_digits(self, login_driver):
        dcp = DeleteCustomerPage(login_driver.driver)
        dcp.set_customer_id("ABC123")
        dcp.click_submit()
        msg = dcp.get_cid_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""

    def test_tc_dc_007_reset_button(self, login_driver):
        dcp = DeleteCustomerPage(login_driver.driver)
        dcp.set_customer_id("12345")
        dcp.click_reset()
        val = dcp.find_element(dcp._cusid_input).get_attribute("value")
        assert val == ""

    def test_tc_dc_008_cid_exceeds_max_length(self, login_driver):
        dcp = DeleteCustomerPage(login_driver.driver)
        el = dcp.find_element(dcp._cusid_input)
        assert el.get_attribute("maxlength") == "10"
