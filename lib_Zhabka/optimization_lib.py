from appium import webdriver


class BasicData:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    platformName = "Android"
    platformVersion = "12.0"
    deviceName = "Zhabka"
    app = "/Users/Lenovo/PycharmProjects/ZhabkaAutoTest/appZhabka/ua4ek.board-release-v2.1.44.apk"
    serverURL = "http://127.0.0.1:4723/wd/hub"

class TextWork:

    def __init__(self, driver: webdriver.Remote):

        self.driver = driver

    t_work = "this step was executed without errors"

    t_not_work = "this step was NOT executed due to an error"

    timeout1 = 1
    timeout2 = 2
    timeout3 = 3
    timeout4 = 4
    timeout5 = 5
    timeout6 = 6
    timeout7 = 7
    timeout8 = 8
    timeout9 = 9
    timeout10 = 10
    timeout11 = 11
    timeout12 = 12
    timeout13 = 13
    timeout14 = 14
    timeout15 = 15
    timeout16 = 16
    timeout17 = 17
    timeout18 = 18
    timeout19 = 19
    timeout20 = 20
