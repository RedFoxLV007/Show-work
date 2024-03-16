from Pages.name_register_page import nameregisterPage
import pytest
from selenium import webdriver
import time



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    base_url = 'https://prosvirov-vladimir.github.io/test-authorization/sign-up.html'
    driver.get(base_url)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.parametrize('username', [('Вячеслав')])
def test_name_register_page(driver, username):
    name_register_page = nameregisterPage(driver)
    name_register_page.name_reg(username)
    time.sleep(5)



