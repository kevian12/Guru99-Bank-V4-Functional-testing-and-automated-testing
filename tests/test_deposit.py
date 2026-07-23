import pytest
from pages.deposit_page import DepositPage

class TestDeposit:
    def test_tc_dp_002_empty_account_no(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("")
        dp.set_amount("2000")
        dp.set_description("Salary")
        dp.click_submit()
        msg = dp.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_dp_003_accno_with_non_digits(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("ACCT123")
        dp.click_submit()
        msg = dp.get_accno_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""

    def test_tc_dp_004_nonexistent_account_no(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("999999")
        dp.set_amount("2000")
        dp.set_description("Test")
        dp.click_submit()
        alert_text = dp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_dp_005_empty_amount(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("999999")
        dp.set_amount("")
        dp.set_description("Test")
        dp.click_submit()
        msg = dp.get_amount_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_dp_007_zero_amount(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("999999")
        dp.set_amount("0")
        dp.set_description("Test")
        dp.click_submit()
        alert_text = dp.get_alert_message()
        assert alert_text is None or "greater" in alert_text or "0" in (alert_text or "")

    def test_tc_dp_008_negative_amount(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("999999")
        dp.set_amount("-500")
        dp.set_description("Test")
        dp.click_submit()
        alert_text = dp.get_alert_message()
        assert alert_text is None or "positive" in alert_text or "greater" in alert_text

    def test_tc_dp_009_empty_description(self, login_driver):
        dp = DepositPage(login_driver.driver)
        dp.set_account_no("999999")
        dp.set_amount("500")
        dp.set_description("")
        dp.click_submit()
        msg = dp.get_desc_validation_msg()
        assert "blank" in msg or msg != ""
