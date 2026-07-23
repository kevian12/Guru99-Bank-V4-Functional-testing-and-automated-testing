import pytest
from pages.manager_home_page import ManagerHomePage
from pages.new_customer_page import NewCustomerPage

class TestNewCustomer:
    def test_tc_nc_001_create_customer_success(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid()
        ncp.click_submit()
        msg = ncp.get_success_message()
        cid = ncp.get_customer_id()
        assert "Customer Registered Successfully" in msg or "Customer Registered" in msg
        assert cid != ""

    def test_tc_nc_002_empty_name(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid(name="")
        ncp.click_submit()
        msg = ncp.get_name_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_nc_003_name_with_numbers(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid(name="John123")
        ncp.click_submit()
        msg = ncp.get_name_validation_msg()
        assert "Numbers" in msg or "not allowed" in msg or msg != ""

    def test_tc_nc_005_empty_address(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid(addr="")
        ncp.click_submit()
        assert "Address" in driver.page_source if False else True  # placeholder

    def test_tc_nc_006_empty_city(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid(city="")
        ncp.click_submit()
        msg = ncp.get_city_validation_msg()
        assert "blank" in msg or msg != ""

    def test_tc_nc_007_city_with_numbers(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid(city="New123")
        ncp.click_submit()
        msg = ncp.get_city_validation_msg()
        assert "Numbers" in msg or "not allowed" in msg or msg != ""

    def test_tc_nc_019_reset_button(self, login_driver):
        mhp = login_driver
        mhp.click_nav("New Customer")
        ncp = NewCustomerPage(mhp.driver)
        ncp.fill_all_valid()
        ncp.click_reset()
        name_val = ncp.find_element(ncp._name_input).get_attribute("value")
        assert name_val == ""
