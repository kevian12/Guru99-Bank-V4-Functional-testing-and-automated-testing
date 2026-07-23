import pytest
from pages.login_page import LoginPage
from pages.manager_home_page import ManagerHomePage

def safe_page_source(driver):
    try:
        return driver.page_source
    except Exception:
        return ""

class TestLogin:
    def test_tc_l_001_successful_login(self, driver):
        lp = LoginPage(driver)
        lp.login("mngr664290", "bUmugas")
        mhp = ManagerHomePage(driver)
        assert "mngr664290" in mhp.get_manager_id()

    def test_tc_l_002_empty_uid(self, driver):
        lp = LoginPage(driver)
        lp.set_uid("")
        lp.set_password("bUmugas")
        lp.click_login()
        alert_text = lp.get_alert_message()
        if alert_text:
            assert "not valid" in alert_text or "blank" in alert_text
        else:
            assert "mngr664290" not in safe_page_source(driver)

    def test_tc_l_003_empty_password(self, driver):
        lp = LoginPage(driver)
        lp.set_uid("mngr664290")
        lp.set_password("")
        lp.click_login()
        alert_text = lp.get_alert_message()
        if alert_text:
            assert "not valid" in alert_text or "blank" in alert_text
        else:
            assert "mngr664290" not in safe_page_source(driver)

    def test_tc_l_004_empty_uid_and_password(self, driver):
        lp = LoginPage(driver)
        lp.set_uid("")
        lp.set_password("")
        lp.click_login()
        alert_text = lp.get_alert_message()
        if alert_text:
            assert "not valid" in alert_text or "blank" in alert_text
        else:
            assert "mngr664290" not in safe_page_source(driver)

    def test_tc_l_005_invalid_uid(self, driver):
        lp = LoginPage(driver)
        lp.login("invalid123", "bUmugas")
        alert_text = lp.get_alert_message()
        assert alert_text is not None and "not valid" in alert_text

    def test_tc_l_006_invalid_password(self, driver):
        lp = LoginPage(driver)
        lp.login("mngr664290", "wrongpass")
        alert_text = lp.get_alert_message()
        assert alert_text is not None and "not valid" in alert_text

    def test_tc_l_007_uid_max_length(self, driver):
        lp = LoginPage(driver)
        uid_input = lp.find_element(lp._uid_input)
        max_len = uid_input.get_attribute("maxlength")
        assert max_len == "10"

    def test_tc_l_008_reset_button(self, driver):
        lp = LoginPage(driver)
        lp.set_uid("mngr664290")
        lp.set_password("bUmugas")
        lp.click_reset()
        uid_val = lp.find_element(lp._uid_input).get_attribute("value")
        pwd_val = lp.find_element(lp._pwd_input).get_attribute("value")
        assert uid_val == "" and pwd_val == ""

    def test_tc_l_009_sql_injection(self, driver):
        lp = LoginPage(driver)
        lp.login("' OR 1=1 --", "test")
        alert_text = lp.get_alert_message()
        assert alert_text is None or "not valid" in alert_text

    def test_tc_l_010_session_after_refresh(self, driver):
        lp = LoginPage(driver)
        lp.login("mngr664290", "bUmugas")
        mhp = ManagerHomePage(driver)
        assert "mngr664290" in mhp.get_manager_id()
        driver.refresh()
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Manger Id')]"))
        )
        mhp2 = ManagerHomePage(driver)
        assert "mngr664290" in mhp2.get_manager_id()
