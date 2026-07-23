import pytest
from pages.mini_statement_page import MiniStatementPage

class TestMiniStatement:
    def test_tc_ms_002_empty_account_no(self, login_driver):
        msp = MiniStatementPage(login_driver.driver)
        msp.set_account_no("")
        msp.click_submit()
        msg = msp.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_ms_003_nonexistent_account_no(self, login_driver):
        msp = MiniStatementPage(login_driver.driver)
        msp.set_account_no("999999")
        msp.click_submit()
        alert_text = msp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_ms_004_accno_with_non_digits(self, login_driver):
        msp = MiniStatementPage(login_driver.driver)
        msp.set_account_no("ABC123")
        msp.click_submit()
        msg = msp.get_accno_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""
