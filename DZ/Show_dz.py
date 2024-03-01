import time
# https://prosvirov-vladimir.github.io/test-authorization/sign-up.html (таблица ТК)
from URL import address_url
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(address_url)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_Register1(driver):
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
    input_elem.send_keys("Вячеслав")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
    input_elem.send_keys("Лис")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[3]")
    input_elem.send_keys("fotibi1171@seosnaps.com")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[4]")
    input_elem.send_keys("qwertyASD123!")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[5]")
    input_elem.send_keys("HP")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/div/div/input")
    input_elem.click()
    input_elem.send_keys("Россия")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[6]")
    input_elem.send_keys("89297970707")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/label/input")
    input_elem.click()
    button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    p_elem = driver.find_element(By.XPATH, "/html/body/div/p")
    p_elem.click()
    driver.save_screenshot("Screen/test_Register1.png")


def test_authorization(driver):
    a_elem = driver.find_element(By.XPATH, "/html/body/div/a")
    a_elem.click()
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
    input_elem.send_keys("fotibi1171@seosnaps.com")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
    input_elem.send_keys("qwertyASD123!")
    button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    driver.save_screenshot("Screen/test_authorization.png")


def test_Register_emptyNAME(driver):
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
    input_elem.send_keys("")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
    input_elem.send_keys("Лис")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[3]")
    input_elem.send_keys("fotibi1171@seosnaps.com")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[4]")
    input_elem.send_keys("qwertyASD123!")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[5]")
    input_elem.send_keys("HP")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/div/div/input")
    input_elem.click()
    input_elem.send_keys("Россия")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[6]")
    input_elem.send_keys("89297970707")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/label/input")
    input_elem.click()
    button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    driver.save_screenshot("Screen/Register_emptyNAME.png")


def test_Register_noCheckBox(driver):
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
    input_elem.send_keys("Вячеслав")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
    input_elem.send_keys("Лис")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[3]")
    input_elem.send_keys("fotibi1171@seosnaps.com")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[4]")
    input_elem.send_keys("qwertyASD123!")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[5]")
    input_elem.send_keys("HP")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/div/div/input")
    input_elem.click()
    input_elem.send_keys("Россия")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[6]")
    input_elem.send_keys("89297970707")
    button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    driver.save_screenshot("Screen/test_Register_noCheckBox.png")


def test_authorization_falled_mail(driver):
    a_elem = driver.find_element(By.XPATH, "/html/body/div/a")
    a_elem.click()
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[1]")
    input_elem.send_keys("fotibi1171@seosnaps123.com")
    input_elem = driver.find_element(By.XPATH, "/html/body/div/form/input[2]")
    input_elem.send_keys("qwertyASD123!")
    button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    driver.save_screenshot("Screen/test_authorization_falled_mail.png")


# ========================== parameterization ================================================
XPATH_locator = "/html/body/div/form/input[6]"


@pytest.mark.parametrize("input_value, expected",
                         [("89297970707", ["89297970707", "Нормальный"]), ("sdfghjkrgh", ["89297970707", "буквы"]),
                          ("1", ["89297970707", "одна цифра!"])])
def test_parameterization_phone(driver, input_value, expected):
    input_elem = driver.find_element(By.XPATH, XPATH_locator)
    input_elem.send_keys(input_value)
    driver.save_screenshot("Screen/test_parameterization_phone.png")  # как делать все скрины при param?
    print(expected)
