from appium import webdriver


class TextOnScreens:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    # text check on the start screen
    t_start_screen = "Вітаємо Вас у додатку"

    # verification of the entered phone
    t_phone_number = "+380 00 001 01 01"

    # location check on the PIN code input screen (1 time)
    t_pin_code_screen1 = "Крок 1 из 2"

    # location check on the PIN code input screen (2 time)
    t_pin_code_screen2 = "Крок 2 из 2"

    # checking the location of the Frog Learner on the screen
    t_learner_screen = "Жабка Навчалка"

    # home screen location check
    t_home_screen = "TOTAL zibrano koshtiv"


class TextForFields:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    # value of the phone number for registration
    t_phone_number = "000010101"

    # value of the confirmation code (from SMS)
    t_sms_code = "000000"

    # value of the PIN code
    t_pin_code = "1111"
