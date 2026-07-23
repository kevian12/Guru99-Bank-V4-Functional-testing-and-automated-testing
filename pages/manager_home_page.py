from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ManagerHomePage(BasePage):
    _welcome_msg = (By.CSS_SELECTOR, "marquee.heading3")
    _manager_id = (By.XPATH, "//td[contains(text(),'Manger Id')]")
    _nav_links = {
        "Manager": (By.LINK_TEXT, "Manager"),
        "New Customer": (By.LINK_TEXT, "New Customer"),
        "Edit Customer": (By.LINK_TEXT, "Edit Customer"),
        "Delete Customer": (By.LINK_TEXT, "Delete Customer"),
        "New Account": (By.LINK_TEXT, "New Account"),
        "Edit Account": (By.LINK_TEXT, "Edit Account"),
        "Delete Account": (By.LINK_TEXT, "Delete Account"),
        "Deposit": (By.LINK_TEXT, "Deposit"),
        "Withdrawal": (By.LINK_TEXT, "Withdrawal"),
        "Fund Transfer": (By.LINK_TEXT, "Fund Transfer"),
        "Change Password": (By.LINK_TEXT, "Change Password"),
        "Balance Enquiry": (By.LINK_TEXT, "Balance Enquiry"),
        "Mini Statement": (By.LINK_TEXT, "Mini Statement"),
        "Customised Statement": (By.LINK_TEXT, "Customised Statement"),
        "Log out": (By.LINK_TEXT, "Log out"),
    }

    def get_welcome_text(self):
        return self.get_text(self._welcome_msg)

    def get_manager_id(self):
        return self.get_text(self._manager_id)

    def click_nav(self, name):
        locator = self._nav_links[name]
        self.click(locator)

    def all_nav_visible(self):
        result = {}
        for name, loc in self._nav_links.items():
            els = self.driver.find_elements(*loc)
            result[name] = len(els) > 0 and els[0].is_displayed()
        return result
