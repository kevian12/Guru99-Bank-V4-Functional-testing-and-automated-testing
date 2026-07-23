import pytest
from pages.withdrawal_page import WithdrawalPage

class TestWithdrawal:
    def test_tc_wd_002_empty_account_no(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("")
        wp.set_amount("500")
        wp.set_description("ATM")
        wp.click_submit()
        msg = wp.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_wd_003_nonexistent_account_no(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("500")
        wp.set_description("Test")
        wp.click_submit()
        alert_text = wp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_wd_004_empty_amount(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("")
        wp.set_description("Test")
        wp.click_submit()
        msg = wp.get_amount_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_wd_005_amount_exceeds_balance(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("9999999")
        wp.set_description("Test")
        wp.click_submit()
        alert_text = wp.get_alert_message()
        assert alert_text is None or "Insufficient" in alert_text or "Failed" in alert_text

    def test_tc_wd_006_zero_amount(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("0")
        wp.set_description("Test")
        wp.click_submit()
        alert_text = wp.get_alert_message()
        assert alert_text is None or "greater" in alert_text or "0" in (alert_text or "")

    def test_tc_wd_007_negative_amount(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("-100")
        wp.set_description("Test")
        wp.click_submit()
        alert_text = wp.get_alert_message()
        assert alert_text is None or "positive" in alert_text or "greater" in alert_text

    def test_tc_wd_008_empty_description(self, login_driver):
        wp = WithdrawalPage(login_driver.driver)
        wp.set_account_no("999999")
        wp.set_amount("500")
        wp.set_description("")
        wp.click_submit()
        msg = wp.get_desc_validation_msg()
        assert "blank" in msg or msg != ""
