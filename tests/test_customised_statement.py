import pytest
from pages.customised_statement_page import CustomisedStatementPage

class TestCustomisedStatement:
    def test_tc_cs_002_empty_account_no(self, login_driver):
        csp = CustomisedStatementPage(login_driver.driver)
        csp.set_account_no("")
        csp.click_submit()
        msg = csp.get_accno_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_cs_003_nonexistent_account_no(self, login_driver):
        csp = CustomisedStatementPage(login_driver.driver)
        csp.set_account_no("999999")
        csp.set_from_date("2026-01-01")
        csp.set_to_date("2026-12-31")
        csp.click_submit()
        alert_text = csp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_cs_004_from_date_after_to_date(self, login_driver):
        csp = CustomisedStatementPage(login_driver.driver)
        csp.set_account_no("999999")
        csp.set_from_date("2026-12-31")
        csp.set_to_date("2026-01-01")
        csp.click_submit()
        alert_text = csp.get_alert_message()
        assert alert_text is None or "invalid" in alert_text or "after" in alert_text
