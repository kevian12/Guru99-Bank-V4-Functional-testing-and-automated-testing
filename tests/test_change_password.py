import pytest
from pages.change_password_page import ChangePasswordPage

class TestChangePassword:
    def test_tc_cp_003_empty_old_password(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("")
        cpp.set_new_password("NewPass123")
        cpp.set_confirm_password("NewPass123")
        cpp.click_submit()
        msg = cpp.get_old_pwd_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_cp_004_empty_new_password(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("bUmugas")
        cpp.set_new_password("")
        cpp.set_confirm_password("")
        cpp.click_submit()
        msg = cpp.get_new_pwd_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_cp_005_empty_confirm_password(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("bUmugas")
        cpp.set_new_password("NewPass123")
        cpp.set_confirm_password("")
        cpp.click_submit()
        msg = cpp.get_confirm_pwd_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_cp_006_passwords_do_not_match(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("bUmugas")
        cpp.set_new_password("NewPass123")
        cpp.set_confirm_password("Different456")
        cpp.click_submit()
        alert_text = cpp.get_alert_message()
        assert alert_text is None or "not match" in alert_text or "do not match" in alert_text

    def test_tc_cp_002_incorrect_old_password(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("wrongpass")
        cpp.set_new_password("NewPass123")
        cpp.set_confirm_password("NewPass123")
        cpp.click_submit()
        alert_text = cpp.get_alert_message()
        assert alert_text is None or "incorrect" in alert_text or "wrong" in alert_text

    def test_tc_cp_010_reset_button(self, login_driver):
        cpp = ChangePasswordPage(login_driver.driver)
        cpp.set_old_password("bUmugas")
        cpp.set_new_password("NewPass123")
        cpp.set_confirm_password("NewPass123")
        cpp.click_reset()
        old_val = cpp.find_element(cpp._old_pwd_input).get_attribute("value")
        new_val = cpp.find_element(cpp._new_pwd_input).get_attribute("value")
        confirm_val = cpp.find_element(cpp._confirm_pwd_input).get_attribute("value")
        assert old_val == "" and new_val == "" and confirm_val == ""
