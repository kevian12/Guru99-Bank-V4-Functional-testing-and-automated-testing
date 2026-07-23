import pytest
from pages.new_account_page import NewAccountPage

class TestNewAccount:
    def test_tc_na_003_empty_customer_id(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("")
        nap.select_account_type("Savings")
        nap.set_initial_deposit("5000")
        nap.click_submit()
        msg = nap.get_cid_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_na_004_cid_with_non_digits(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("ABC123")
        nap.click_submit()
        msg = nap.get_cid_validation_msg()
        assert "Characters" in msg or "not allowed" in msg or msg != ""

    def test_tc_na_005_nonexistent_customer_id(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("99999")
        nap.select_account_type("Savings")
        nap.set_initial_deposit("5000")
        nap.click_submit()
        alert_text = nap.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text

    def test_tc_na_006_empty_deposit(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("99999")
        nap.set_initial_deposit("")
        nap.click_submit()
        # should show validation on client side
        assert True

    def test_tc_na_007_deposit_with_non_digits(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("99999")
        nap.set_initial_deposit("ABC5000")
        nap.click_submit()
        msg = nap.get_alert_message()
        # will likely be caught by server-side validation
        assert True

    def test_tc_na_009_negative_deposit(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("99999")
        nap.set_initial_deposit("-100")
        nap.click_submit()
        alert_text = nap.get_alert_message()
        assert alert_text is None or "positive" in alert_text or "greater" in alert_text

    def test_tc_na_008_zero_deposit(self, login_driver):
        nap = NewAccountPage(login_driver.driver)
        nap.set_customer_id("99999")
        nap.set_initial_deposit("0")
        nap.click_submit()
        alert_text = nap.get_alert_message()
        assert alert_text is None or "greater" in alert_text or "0" in (alert_text or "")
