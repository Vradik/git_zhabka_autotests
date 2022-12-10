from appium import webdriver
from lib_Zhabka.locators_lib import Locators
import time

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "Zhabka",
    "app": "/Users/Lenovo/PycharmProjects/ZhabkaAutoTest/appZhabka/ua4ek.board-release-v2.1.44.apk"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

p1 = Locators(driver)

# перевірка тексту (наявність певного тексту на екрані)
text2 = p1.text_greeting.text
text1 = "Вітаємо Вас у додатку"
if text1==text2:
    print("App is started")
else:
    print("App is NOT started")
time.sleep(5)


# введення номеру телефона
inputElement = p1.input_Phone_Registration.send_keys('000010101')
time.sleep(5)

# перевірка введеного телефону
phone_numb2 = p1.input_Phone_Registration.text
phone_numb1 = "+380 00 001 01 01"
if phone_numb1==phone_numb2:
    print("Phone number is entered")
else:
    print("Phone number is NOT entered")
time.sleep(5)

# натискання кнопки Далі (після того, як успішно введено номер телефону)
p1.start_button.click()
time.sleep(10)
