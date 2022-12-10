from appium import webdriver
from selenium.webdriver.common.by import By



class Locators (object):
    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    @property
    def input_Phone_Registration(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/editPhone')

    @property
    def text_greeting(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/greeting')

    @property
    def start_button(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/lets_start_button')

    @property
    def StartAPP(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/editPhone')
