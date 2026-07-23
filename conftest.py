import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from test_data.config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # 取消注释可启用无头模式
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_driver(driver):
    driver.get(BASE_URL)
    from pages.login_page import LoginPage
    lp = LoginPage(driver)
    lp.login("mngr664290", "bUmugas")
    from pages.manager_home_page import ManagerHomePage
    return ManagerHomePage(driver)
