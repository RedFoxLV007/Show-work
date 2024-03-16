from selenium.webdriver.common.by import By


class nameregisterPage:
    def __init__(self,driver):
        self.username = driver.find_element(By.XPATH, '/html/body/div/form/input[1]')

    def name_reg(self, username: str, password: str = ''):
        self.username.send_keys(username)




