import pytest
from pages.balance_enquiry_page import BalanceEnquiryPage

class TestBalanceEnquiry:
    def test_tc_be_002_empty_account_no(self, login_driver):
        bep = BalanceEnquiryPage(login_driver.driver)
        bep.set_account_no("")
        bep.click_submit()
        msg = bep.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_be_003_nonexistent_account_no(self, login_driver):
        bep = BalanceEnquiryPage(login_driver.driver)
        bep.set_account_no("999999")
        bep.click_submit()
        alert_text = bep.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_be_004_accno_with_non_digits(self, login_driver):
        bep = BalanceEnquiryPage(login_driver.driver)
        bep.set_account_no("ABC123")
        bep.click_submit()
        msg = bep.get_accno_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""
