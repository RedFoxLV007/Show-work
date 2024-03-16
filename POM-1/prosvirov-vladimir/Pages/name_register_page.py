from .Locators import *


class nameregisterPage:
    def __init__(self,driver):
        self.username = driver.find_element(*username)
        self.lastName_locator = driver.find_element(*lastName_locator)
        self.userEmail_locator = driver.find_element(*userEmail_locator)
        self.userPassword_locator = driver.find_element(*userPassword_locator)
        self.userCompany_locator = driver.find_element(*userCompany_locator)

    def name_reg(self, username:str = '', lastName_locator:str = '', userEmail_locator:str = '',userPassword_locator:str = '',userCompany_locator:str = ''):
        self.username.send_keys(username)
        self.lastName_locator.send_keys(lastName_locator)
        self.userEmail_locator.send_keys(userEmail_locator)
        self.userPassword_locator.send_keys(userPassword_locator)
        self.userCompany_locator.send_keys(userCompany_locator)




