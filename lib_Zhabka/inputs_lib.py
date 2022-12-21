from appium import webdriver


class TextOnScreens:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    # text check on the start screen
    t_home_screen = "Вітаємо Вас у додатку"


class TextForFields:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    # value of the phone number for registration
    t_phone_number = "000010101"
