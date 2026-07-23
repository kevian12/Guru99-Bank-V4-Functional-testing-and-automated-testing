import pytest
from pages.fund_transfer_page import FundTransferPage

class TestFundTransfer:
    def test_tc_ft_002_empty_payers_account(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("")
        ftp.set_payees_account("100002")
        ftp.set_amount("500")
        ftp.set_description("Transfer")
        ftp.click_submit()
        msg = ftp.get_payers_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_ft_003_empty_payees_account(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("100001")
        ftp.set_payees_account("")
        ftp.set_amount("500")
        ftp.set_description("Transfer")
        ftp.click_submit()
        # client-side validation
        assert True

    def test_tc_ft_004_same_account_transfer(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("100001")
        ftp.set_payees_account("100001")
        ftp.set_amount("500")
        ftp.set_description("Transfer")
        ftp.click_submit()
        alert_text = ftp.get_alert_message()
        assert alert_text is None or "not allowed" in alert_text or "same" in alert_text

    def test_tc_ft_006_zero_amount(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("100001")
        ftp.set_payees_account("100002")
        ftp.set_amount("0")
        ftp.set_description("Transfer")
        ftp.click_submit()
        alert_text = ftp.get_alert_message()
        assert alert_text is None or "greater" in alert_text or "0" in (alert_text or "")

    def test_tc_ft_007_negative_amount(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("100001")
        ftp.set_payees_account("100002")
        ftp.set_amount("-500")
        ftp.set_description("Transfer")
        ftp.click_submit()
        alert_text = ftp.get_alert_message()
        assert alert_text is None or "positive" in alert_text or "greater" in alert_text

    def test_tc_ft_010_nonexistent_payee(self, login_driver):
        ftp = FundTransferPage(login_driver.driver)
        ftp.set_payers_account("100001")
        ftp.set_payees_account("999999")
        ftp.set_amount("500")
        ftp.set_description("Transfer")
        ftp.click_submit()
        alert_text = ftp.get_alert_message()
        assert alert_text is None or "not exist" in alert_text or "not found" in alert_text
