import pytest
from pages.manager_home_page import ManagerHomePage

class TestManagerHomepage:
    def test_tc_h_001_page_display(self, login_driver):
        mhp = login_driver
        assert "Guru99 Bank Manager HomePage" in mhp.driver.title
        assert "mngr664290" in mhp.get_manager_id()

    def test_tc_h_002_nav_menu_completeness(self, login_driver):
        mhp = login_driver
        nav = mhp.all_nav_visible()
        expected = ["Manager", "New Customer", "Edit Customer", "Delete Customer",
                    "New Account", "Edit Account", "Delete Account", "Deposit",
                    "Withdrawal", "Fund Transfer", "Change Password",
                    "Balance Enquiry", "Mini Statement", "Customised Statement",
                    "Log out"]
        for name in expected:
            assert nav.get(name), f"{name} not visible"

    def test_tc_h_003_nav_links_clickable(self, login_driver):
        mhp = login_driver
        links = {
            "New Customer": "addcustomerpage",
            "Deposit": "DepositInput",
            "Balance Enquiry": "BalEnqInput",
        }
        for name, keyword in links.items():
            mhp.click_nav(name)
            assert keyword in mhp.driver.current_url or keyword in mhp.driver.page_source
            mhp.click_nav("Manager")
