from appium import webdriver
from lib_Zhabka.locators_lib import Locators
from lib_Zhabka.optimization_lib import TextWork
from lib_Zhabka.inputs_lib import TextOnScreens
from lib_Zhabka.inputs_lib import TextForFields
import time

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "12.0",
    "deviceName": "Zhabka",
    "app": "/Users/Lenovo/PycharmProjects/ZhabkaAutoTest/appZhabka/ua4ek.board-release-v2.1.44.apk"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

locators1 = Locators(driver)
optimization1 = TextWork(driver)
inputs1 = TextOnScreens(driver)
inputs2 = TextForFields(driver)


# text check (presence of certain text on the screen)
text1 = inputs1.t_home_screen
text2 = locators1.text_greeting.text
if text1==text2:
    print("text_greeting - " + optimization1.t_work)
else:
    print("text_greeting - " + optimization1.t_not_work)
time.sleep(optimization1.timeout7)


# entering a phone number
inputElement = locators1.input_phone.send_keys(inputs2.t_phone_number)
time.sleep(5)


# verification of the entered phone
phone_numb1 = "+380 00 001 01 01"
phone_numb2 = locators1.input_phone.text
if phone_numb1==phone_numb2:
    print("Phone number is entered")
else:
    print("Phone number is NOT entered")
time.sleep(5)


# clicking the Next button (after the phone number has been successfully entered)
locators1.confirmation_phone_numb.click()
time.sleep(10)


# entering a confirmation code (from SMS)
inputElement = locators1.code_sms.send_keys('000000')
time.sleep(7)


# verification of the entered confirmation code (from SMS)
# code_numb1 = "000000"
# code_numb2 = locators1.code_sms.text
# if code_numb1==code_numb2:
    # print("Code number is entered")
# else:
    # print("Code number is NOT entered")
# time.sleep(5)


# location check on the PIN code input screen (1 time)
pin_code1 = "Крок 1 из 2"
pin_code2 = locators1.code_pin_1_screen.text
if pin_code1==pin_code2:
    print("Screen for 1 step pin is displayed")
else:
    print("Screen for 1 step pin is NOT displayed")


# PIN code entry (first time)
inputElement = locators1.code_pin.send_keys('1111')
time.sleep(5)


# location check on the PIN code input screen (2 time)
pin_code1 = "Крок 2 из 2"
pin_code2 = locators1.code_pin_2_screen.text
if pin_code1==pin_code2:
    print("Screen for 2 step pin is displayed")
else:
    print("Screen for 2 step pin is NOT displayed")


# PIN code entry (second time)
inputElement = locators1.code_pin.send_keys('1111')
time.sleep(10)


# checking the location of the Frog Learner on the screen
study1 = "Жабка Навчалка"
study2 = locators1.chat_screen.text
if study1==study2:
    print("Screen for Intro is displayed")
else:
    print("Screen for Intro is NOT displayed")


# skip training (go to the main menu)
locators1.skip_chat.click()
time.sleep(5)


# home screen location check
home1 = "TOTAL zibrano koshtiv"
home2 = locators1.main_screen.text
if home1==home2:
    print("Home screen is displayed")
else:
    print("Home screen is NOT displayed")
time.sleep(5)
