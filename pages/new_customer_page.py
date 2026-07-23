from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NewCustomerPage(BasePage):
    _name_input = (By.NAME, "name")
    _gender_radio_m = (By.XPATH, "//input[@name='rad1' and @value='m']")
    _gender_radio_f = (By.XPATH, "//input[@name='rad1' and @value='f']")
    _dob_input = (By.NAME, "dob")
    _addr_textarea = (By.NAME, "addr")
    _city_input = (By.NAME, "city")
    _state_input = (By.NAME, "state")
    _pin_input = (By.NAME, "pinno")
    _mobile_input = (By.NAME, "telephoneno")
    _email_input = (By.NAME, "emailid")
    _pwd_input = (By.NAME, "password")
    _submit_btn = (By.NAME, "sub")
    _reset_btn = (By.NAME, "res")
    _name_msg = (By.ID, "message")
    _addr_msg = (By.ID, "message3")
    _city_msg = (By.ID, "message4")
    _state_msg = (By.ID, "message5")
    _pin_msg = (By.ID, "message6")
    _mobile_msg = (By.ID, "message7")
    _email_msg = (By.ID, "message9")
    _pwd_msg = (By.ID, "message18")
    _dob_msg = (By.ID, "message24")
    _success_heading = (By.XPATH, "//p[@class='heading3']")
    _customer_id_text = (By.XPATH, "//td[contains(text(),'Customer ID')]/following-sibling::td")

    def set_name(self, name):
        self.send_keys(self._name_input, name)

    def set_gender(self, gender):
        if gender.lower() == "male":
            self.click(self._gender_radio_m)
        else:
            self.click(self._gender_radio_f)

    def set_dob(self, dob):
        self.send_keys(self._dob_input, dob)

    def set_address(self, addr):
        self.send_keys(self._addr_textarea, addr)

    def set_city(self, city):
        self.send_keys(self._city_input, city)

    def set_state(self, state):
        self.send_keys(self._state_input, state)

    def set_pin(self, pin):
        self.send_keys(self._pin_input, pin)

    def set_mobile(self, mobile):
        self.send_keys(self._mobile_input, mobile)

    def set_email(self, email):
        self.send_keys(self._email_input, email)

    def set_password(self, pwd):
        self.send_keys(self._pwd_input, pwd)

    def click_submit(self):
        self.click(self._submit_btn)

    def click_reset(self):
        self.click(self._reset_btn)

    def fill_all_valid(self, **overrides):
        data = dict(name="John Smith", gender="male", dob="1990-01-15",
                    addr="123 Main St", city="New York", state="NY",
                    pin="500001", mobile="9876543210", email="john@test.com",
                    password="test123")
        data.update(overrides)
        self.set_name(data["name"])
        self.set_gender(data["gender"])
        self.set_dob(data["dob"])
        self.set_address(data["addr"])
        self.set_city(data["city"])
        self.set_state(data["state"])
        self.set_pin(data["pin"])
        self.set_mobile(data["mobile"])
        self.set_email(data["email"])
        self.set_password(data["password"])

    def get_name_validation_msg(self):
        return self.get_text(self._name_msg) if self.driver.find_elements(*self._name_msg) else ""

    def get_city_validation_msg(self):
        return self.get_text(self._city_msg) if self.driver.find_elements(*self._city_msg) else ""

    def get_success_message(self):
        return self.get_text(self._success_heading) if self.driver.find_elements(*self._success_heading) else ""

    def get_customer_id(self):
        return self.get_text(self._customer_id_text) if self.driver.find_elements(*self._customer_id_text) else ""
