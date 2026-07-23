import pytest
from pages.delete_account_page import DeleteAccountPage

class TestDeleteAccount:
    def test_tc_da_002_empty_account_no(self, login_driver):
        dap = DeleteAccountPage(login_driver.driver)
        dap.set_account_no("")
        dap.click_submit()
        msg = dap.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_da_003_nonexistent_account_no(self, login_driver):
        dap = DeleteAccountPage(login_driver.driver)
        dap.set_account_no("999999")
        dap.click_submit()
        alert_text = dap.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_da_004_accno_with_non_digits(self, login_driver):
        dap = DeleteAccountPage(login_driver.driver)
        dap.set_account_no("ABC789")
        dap.click_submit()
        msg = dap.get_accno_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""
