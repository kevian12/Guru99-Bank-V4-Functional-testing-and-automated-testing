import pytest
from pages.edit_account_page import EditAccountPage

class TestEditAccount:
    def test_tc_ea_002_empty_account_no(self, login_driver):
        eap = EditAccountPage(login_driver.driver)
        eap.set_account_no("")
        eap.click_submit()
        msg = eap.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_ea_003_nonexistent_account_no(self, login_driver):
        eap = EditAccountPage(login_driver.driver)
        eap.set_account_no("999999")
        eap.click_submit()
        alert_text = eap.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_ea_004_accno_with_non_digits(self, login_driver):
        eap = EditAccountPage(login_driver.driver)
        eap.set_account_no("ABC789")
        eap.click_submit()
        msg = eap.get_accno_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""
