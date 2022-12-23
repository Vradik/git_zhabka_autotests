from appium import webdriver
from lib_Zhabka.locators_lib import Locators
from lib_Zhabka.optimization_lib import TextWork
from lib_Zhabka.optimization_lib import BasicData
from lib_Zhabka.inputs_lib import TextOnScreens
from lib_Zhabka.inputs_lib import TextForFields
import time


desired_capabilities = {
    "platformName": BasicData.platformName,
    "platformVersion": BasicData.platformVersion,
    "deviceName": BasicData.deviceName,
    "app": BasicData.app}
driver = webdriver.Remote(BasicData.serverURL, desired_capabilities=desired_capabilities)


locators1 = Locators(driver)
optimization1 = TextWork(driver)
inputs1 = TextOnScreens(driver)
inputs2 = TextForFields(driver)


# text check (presence of certain text on the screen)
data1 = inputs1.t_start_screen
data2 = locators1.text_greeting.text
if data1==data2:
    print("text_greeting - " + optimization1.t_work)
else:
    print("text_greeting - " + optimization1.t_not_work)
time.sleep(optimization1.timeout7)


# entering a phone number
inputElement = locators1.input_phone.send_keys(inputs2.t_phone_number)
time.sleep(optimization1.timeout5)


# verification of the entered phone
data1 = inputs1.t_phone_number
data2 = locators1.input_phone.text
if data1==data2:
    print("input_phone - " + optimization1.t_work)
else:
    print("input_phone - " + optimization1.t_not_work)
time.sleep(optimization1.timeout5)


# clicking the Next button (after the phone number has been successfully entered)
locators1.confirmation_phone_numb.click()
time.sleep(optimization1.timeout10)


# entering a confirmation code (from SMS)
inputElement = locators1.code_sms.send_keys(inputs2.t_sms_code)
time.sleep(optimization1.timeout7)


# location check on the PIN code input screen (1 time)
data1 = inputs1.t_pin_code_screen1
data2 = locators1.code_pin_1_screen.text
if data1==data2:
    print("code_pin_1_screen - " + optimization1.t_work)
else:
    print("code_pin_1_screen - " + optimization1.t_not_work)


# PIN code entry (first time)
inputElement = locators1.code_pin.send_keys(inputs2.t_pin_code)
time.sleep(optimization1.timeout5)


# location check on the PIN code input screen (2 time)
data1 = inputs1.t_pin_code_screen2
data2 = locators1.code_pin_2_screen.text
if data1==data2:
    print("code_pin_2_screen - " + optimization1.t_work)
else:
    print("code_pin_2_screen - " + optimization1.t_not_work)


# PIN code entry (second time)
inputElement = locators1.code_pin.send_keys(inputs2.t_pin_code)
time.sleep(optimization1.timeout10)


# checking the location of the Frog Learner on the screen
data1 = inputs1.t_learner_screen
data2 = locators1.chat_screen.text
if data1==data2:
    print("chat_screen - " + optimization1.t_work)
else:
    print("chat_screen - " + optimization1.t_not_work)


# skip training (go to the main menu)
locators1.skip_chat.click()
time.sleep(optimization1.timeout5)


# home screen location check
data1 = inputs1.t_home_screen
data2 = locators1.main_screen.text
if data1==data2:
    print("main_screen - " + optimization1.t_work)
else:
    print("main_screen - " + optimization1.t_not_work)
time.sleep(optimization1.timeout5)
