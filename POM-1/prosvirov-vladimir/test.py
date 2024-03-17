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


@pytest.mark.parametrize('username ,lastName_locator,userEmail_locator,userPassword_locator,userCompany_locator,userCountry_locator,userPhone_locator', [('Вячеслав','Лис','fotibi1171@seosnaps.com','qwertyASD123!','HP','Россия','89297970707')])
def test_name_register_page(driver, username,lastName_locator,userEmail_locator,userPassword_locator,userCompany_locator,userCountry_locator,userPhone_locator):
    name_register_page = nameregisterPage(driver)
    name_register_page.name_reg(username,lastName_locator,userEmail_locator,userPassword_locator,userCompany_locator,userCountry_locator,userPhone_locator)
    driver.save_screenshot("Screens/test_register_page.png")
    time.sleep(5)



